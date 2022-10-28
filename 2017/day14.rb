# Day 14: Disk Defragmentation

require 'test/unit/assertions'

include Test::Unit::Assertions

INPUT_KEY = "vbqugkhl"
TEST_INPUT_KEY = "flqrgnkx"
DISPLACEMENTS = [[1, 0], [-1, 0], [0, -1], [0, 1]]

def perform_knot_hash(values, length_nums, num_rounds = 1)
  # Performs the knot hash procedure given a circular list of values and a list
  # of lengths. The number of rounds can be customized and is defaulted to 1.

  # For each length and given a position and skip size
  #   Reverses the order of the length of elements starting at the specified position
  #   Position moves forward by the length and skip size
  #   Skip size is incremented by 1

  position = 0
  skip_size = 0

  num_rounds.times do 
    length_nums.each do |length_num|
      sublist = values[position, length_num]
  
      if (sublist.length < length_num) 
        sublist.concat(values[0, length_num - sublist.length])
      end 

      sublist_reversed = sublist.reverse
      sublist_reversed.each_with_index do |num, index|
        values[(position + index) % values.length] = num
      end
      position = (position + length_num + skip_size) % values.length
      skip_size += 1
    end
  end
end

def get_dense_hash(sparse_hash)
  # Reduces a list of numbers called a sparse hash into a dense hash in 
  # binary form.

  # To reduce the sparse hash, each block of 16 numbers is reduced into
  # one number by XOR-ing the values in the block.

  dense_hash = ""
  pos = 0
  while (pos < sparse_hash.length)
    block = sparse_hash[pos, 16]
    block_hash = block[0]
    block.each_with_index { |num, index| block_hash ^= num unless index == 0 }
    dense_hash << block_hash.to_s(2).rjust(8, "0")
    pos += 16
  end
  dense_hash
end

def get_used_squares(key)
  # Returns an array of the locations of the used squares in the disk 128x128 grid
  # To get each row's state, the knot hash is calculated using the hash
  # input in the form of: key-rowNum

  used_squares = []

  rows = (0...128).to_a
  rows.each do |row_num|
    values = (0...256).to_a
    hash_input = "#{key}-#{row_num}"
    length_nums = []
    hash_input.each_byte { |byte_num| length_nums << byte_num }
    length_nums.concat([17, 31, 73, 47, 23])
    perform_knot_hash(values, length_nums, 64)
    dense_hash = get_dense_hash(values)
    dense_hash.split("").each_with_index { |c, index| used_squares << [row_num, index] if c == "1" }
  end

  used_squares
end

def get_num_regions(used_squares)
  # Returns the number of regions, which is a group of used squares 
  # that are adjacent to each other either vertically or horizontally 

  num_regions = 0

  seen = []
  used_squares.each do |square_position|
    next if seen.include?(square_position)
    
    region_queue = [square_position]
    until region_queue.empty?
      curr_square = region_queue.shift
      next if seen.include?(curr_square)
      seen << curr_square

      curr_row, curr_col = curr_square
      DISPLACEMENTS.each do |disp|
        disp_row, disp_col = disp
        next_position = [curr_row + disp_row, curr_col + disp_col]
        region_queue << next_position if used_squares.include?(next_position)
      end
    end

    num_regions += 1
  end

  num_regions
end

def solve(key)
  # Returns an array of the number of used squares and number of regions 
  # in the disk 128x128 grid.
  used_squares = get_used_squares(key)
  num_regions = get_num_regions(used_squares)
  [used_squares.length, num_regions]
end

def main
  test_num_used_squares, test_num_regions = solve(TEST_INPUT_KEY)
  assert test_num_used_squares == 8108
  assert test_num_regions == 1242

  num_used_squares, num_regions = solve(INPUT_KEY)
  puts "Part One: #{num_used_squares}"
  puts "Part Two: #{num_regions}"
end

main