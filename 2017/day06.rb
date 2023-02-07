# Day 6: Memory Reallocation

require 'test/unit/assertions'

include Test::Unit::Assertions

INPUT_FILE_NAME = "./inputs/day06input.txt"

TEST_MEMORY_BANKS = [0, 2, 7, 0]

def get_memory_banks(file_nm)
  # Reads a file and returns a list of the number of blocks in 
  # the 16 memory banks

  memory_banks = nil
  File.open(file_nm).each do |line|
    memory_banks = line.chomp.split("\t").map { |num_blocks| num_blocks.to_i }
  end
  return memory_banks
end

def find_max_memory_bank(memory_banks)
  # Returns the bank index that has the most number of blocks

  max_index = 0
  max_num_blocks = 0
  memory_banks.each_with_index do |num_blocks, i|
    if (num_blocks > max_num_blocks)
      max_index = i
      max_num_blocks = num_blocks
    end
  end
  max_index
end

def solve(memory_banks)
  # Returns the number of redistribution cycles before reproducing a bank
  # configuration and returns the amount of cycles it takes to encounter
  # a repeated configuration

  # In each cycle, the bank with the most blocks has its blocks redistributed 
  # starting from the bank located after it. 

  seen = []
  cycle_count = 0

  until seen.include?(memory_banks)
    seen << memory_banks.dup
    max_index = find_max_memory_bank(memory_banks)
    num_blocks = memory_banks[max_index]
    memory_banks[max_index] = 0
    distribute_index = (max_index + 1) % memory_banks.length
    until (num_blocks == 0)
      memory_banks[distribute_index] += 1
      distribute_index = (distribute_index + 1) % memory_banks.length
      num_blocks -= 1
    end
    cycle_count += 1
  end

  [cycle_count, cycle_count - seen.index(memory_banks)]
end

def main
  test_cycle_count, test_cycles_seen_again = solve(TEST_MEMORY_BANKS)
  assert test_cycle_count == 5
  assert test_cycles_seen_again == 4

  memory_banks = get_memory_banks(INPUT_FILE_NAME)
  cycle_count, cycles_seen_again = solve(memory_banks)
  puts "Part One: #{cycle_count}"
  puts "Part Two: #{cycles_seen_again}"
end

main