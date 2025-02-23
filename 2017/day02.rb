# Day 2: Corruption Checksum

require 'test/unit/assertions'

include Test::Unit::Assertions

INPUT_FILE_NAME = "./inputs/day02input.txt"

# Reads a file and returns the rows of random numbers
def get_spreadsheet_numbers(file_nm)
  arr = []
  File.open(file_nm).each do |line|
    arr << line.chomp.split("\t").map { |num| num.to_i }
  end
  return arr
end

# Returns the spreadsheet's checksum by taking the sum of all 
# the differences of the largest and smallest value in each row
def calculate_checksum(spreadsheet_numbers)
  sum = 0
  spreadsheet_numbers.each { |row| sum += row.max - row.min }
  return sum
end

# Returns the sum of quotients of the pair of numbers in each row
# where one evenly divides the other.
def calculate_evenly_divisble_quotients_sum(spreadsheet_numbers)
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
  if File.exist?(INPUT_FILE_NAME)
    spreadsheet_numbers = get_spreadsheet_numbers(INPUT_FILE_NAME)
    puts "Part One: #{solve_part_one(spreadsheet_numbers)}"
    puts "Part Two: #{solve_part_two(spreadsheet_numbers)}"
  end
end

main