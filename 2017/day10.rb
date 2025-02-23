# Day 10: Knot Hash

INPUT_FILE_NAME = "./inputs/day10input.txt"
NUM_ROUNDS_PART_TWO = 64

# Reads a file and returns the contents representing the lengths.
def get_lengths_input(file_nm)
  lengths_input = nil
  File.open(file_nm) do |file|
    lengths_input = file.first.chomp
  end
  return lengths_input
end

# Performs the knot hash procedure given a circular list of values and a list
# of lengths. The number of rounds can be customized and is defaulted to 1.

# For each length and given a position and skip size
#   Reverses the order of the length of elements starting at the specified position
#   Position moves forward by the length and skip size
#   Skip size is incremented by 1
def perform_knot_hash(values, length_nums, num_rounds = 1)
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

# Reduces a list of numbers called a sparse hash into a dense hash in 
# hexadecimal form.

# To reduce the sparse hash, each block of 16 numbers is reduced into
# one number by XOR-ing the values in the block.
def get_dense_hash(sparse_hash)
  dense_hash = ""
  pos = 0
  while (pos < sparse_hash.length)
    block = sparse_hash[pos, 16]
    block_hash = block[0]
    block.each_with_index { |num, index| block_hash ^= num unless index == 0 }
    dense_hash << block_hash.to_s(16).rjust(2, "0")
    pos += 16
  end

  dense_hash
end

# Returns the product of the first two values in our list of 256 numbers
# after performing knot hash one time.

# The lengths input is read as a list of numbers.
def solve_part_one(lengths_input)
  length_nums = lengths_input.split(",").map { |num| num.to_i }
  values = (0...256).to_a
  perform_knot_hash(values, length_nums)
  values[0] * values[1]
end

# Returns the dense hash in hexadecimal form after performing knot hash 
# x number of times.

# The lengths input is read as a list of bytes and 17, 31, 73, 47, 23
# are added at the end of the lengths sequence.
def solve_part_two(lengths_input, num_rounds)
  values = (0...256).to_a
  length_nums = []
  lengths_input.each_byte { |byte_num| length_nums << byte_num }
  length_nums.concat([17, 31, 73, 47, 23])

  perform_knot_hash(values, length_nums, num_rounds)
  get_dense_hash(values)
end

def main
  lengths = get_lengths_input(INPUT_FILE_NAME)
  puts "Part One: #{solve_part_one(lengths)}"
  puts "Part Two: #{solve_part_two(lengths, NUM_ROUNDS_PART_TWO)}"
end

if __FILE__==$0
  main
end