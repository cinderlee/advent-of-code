# Day 2: Corruption Checksum

require 'test/unit/assertions'

include Test::Unit::Assertions

INPUT_FILE_NAME = "./inputs/day02input.txt"
TEST_INPUT = [
  [5, 1, 9, 5],
  [7, 5, 3],
  [2, 4, 6, 8]
]
TEST_INPUT_2 = [
  [5, 9, 2, 8],
  [9, 4, 7, 3],
  [3, 8, 6, 5]
]

def get_spreadsheet_numbers(file_nm)
  # Reads a file and returns the rows of random numbers

  arr = []
  File.open(file_nm).each do |line|
    arr << line.chomp.split("\t").map { |num| num.to_i }
  end
  return arr
end

def calculate_checksum(spreadsheet_numbers)
  # Returns the spreadsheet's checksum by taking the sum of all 
  # the differences of the largest and smallest value in each row

  sum = 0
  spreadsheet_numbers.each { |row| sum += row.max - row.min }
  return sum
end

def calculate_evenly_divisble_quotients_sum(spreadsheet_numbers)
  # Returns the sum of quotients of the pair of numbers in each row
  # where one evenly divides the other.

  sum = 0
  spreadsheet_numbers.each do |row|
    (0...row.length).each do |index|
      (index + 1 ... row.length).each do |other_index|
        if row[index] % row[other_index] == 0
          sum += row[index] / row[other_index]
        elsif row[other_index] % row[index] == 0
          sum += row[other_index] / row[index]
        end
      end
    end
  end
  return sum
end

def solve_part_one(spreadsheet_numbers)
  calculate_checksum(spreadsheet_numbers)
end

def solve_part_two(spreadsheet_numbers)
  calculate_evenly_divisble_quotients_sum(spreadsheet_numbers)
end

def main
  assert solve_part_one(TEST_INPUT) == 18
  assert solve_part_two(TEST_INPUT_2) == 9

  spreadsheet_numbers = get_spreadsheet_numbers(INPUT_FILE_NAME)
  puts "Part One: #{solve_part_one(spreadsheet_numbers)}"
  puts "Part Two: #{solve_part_two(spreadsheet_numbers)}"
end

main