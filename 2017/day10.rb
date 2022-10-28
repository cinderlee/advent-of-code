# Day 10: Knot Hash

require 'test/unit/assertions'

include Test::Unit::Assertions

INPUT_FILE_NAME = "./inputs/day10input.txt"
NUM_ROUNDS_PART_TWO = 64

TEST_VALUES = [0, 1, 2, 3, 4]
TEST_LENGTHS = [3, 4, 1, 5]

TEST_LENGTHS_INPUT_1 = ""
TEST_LENGTHS_INPUT_2 = "AoC 2017"
TEST_LENGTHS_INPUT_3 = "1,2,3"
TEST_LENGTHS_INPUT_4 = "1,2,4"

def get_lengths_input(file_nm)
  # Reads a file and returns the contents representing the lengths.

  lengths_input = nil
  File.open(INPUT_FILE_NAME) do |file|
    lengths_input = file.first.chomp
  end
  return lengths_input
end

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
  # hexadecimal form.

  # To reduce the sparse hash, each block of 16 numbers is reduced into
  # one number by XOR-ing the values in the block.

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

def solve_part_one(lengths_input)
  # Returns the product of the first two values in our list of 256 numbers
  # after performing knot hash one time.

  # The lengths input is read as a list of numbers.

  length_nums = lengths_input.split(",").map { |num| num.to_i }
  values = (0...256).to_a
  perform_knot_hash(values, length_nums)
  values[0] * values[1]
end

def solve_part_two(lengths_input, num_rounds)
  # Returns the dense hash in hexadecimal form after performing knot hash 
  # x number of times.

  # The lengths input is read as a list of bytes and 17, 31, 73, 47, 23
  # are added at the end of the lengths sequence.

  values = (0...256).to_a
  length_nums = []
  lengths_input.each_byte { |byte_num| length_nums << byte_num }
  length_nums.concat([17, 31, 73, 47, 23])

  perform_knot_hash(values, length_nums, num_rounds)
  get_dense_hash(values)
end

def main
  perform_knot_hash(TEST_VALUES, TEST_LENGTHS)
  assert TEST_VALUES == [3, 4, 2, 1, 0]

  assert solve_part_two(TEST_LENGTHS_INPUT_1, NUM_ROUNDS_PART_TWO) == "a2582a3a0e66e6e86e3812dcb672a272"
  assert solve_part_two(TEST_LENGTHS_INPUT_2, NUM_ROUNDS_PART_TWO) == "33efeb34ea91902bb2f59c9920caa6cd"
  assert solve_part_two(TEST_LENGTHS_INPUT_3, NUM_ROUNDS_PART_TWO) == "3efbe78a8d82f29979031a4aa0b16a9d"
  assert solve_part_two(TEST_LENGTHS_INPUT_4, NUM_ROUNDS_PART_TWO) == "63960835bcdc130f0b66d7ff4f6a5a8e"

  lengths = get_lengths_input(INPUT_FILE_NAME)
  puts "Part One: #{solve_part_one(lengths)}"
  puts "Part Two: #{solve_part_two(lengths, NUM_ROUNDS_PART_TWO)}"
end

main