# Day 1: Inverse Captcha

require "minitest/autorun"

INPUT_FILE_NAME = "./inputs/day01input.txt"

# Reads a file and returns the sequence of digits (on the first line)
def get_digits_sequence(file_nm)
  sequence = nil
  File.open(file_nm) do |file|
    sequence = file.first
  end
  return sequence
end

# Solves a captcha by finding the sum of all digits in the sequence
# that match the next digit. The sequence is circular so the next
# digit after the last will be the first digit.
def solve_captcha(digits_sequence)
  sum = 0
  num_digits = digits_sequence.length
  (0...num_digits).each do |index|
    if digits_sequence[index] == digits_sequence[(index + 1) % num_digits]
      sum += digits_sequence[index].to_i
    end
  end 
  return sum
end

# Solves a captcha by finding the sum of all digits in the sequence
# that match the digit halfway around the circular sequence.
def solve_captcha_half(digits_sequence)
  sum = 0
  num_digits = digits_sequence.length
  (0...num_digits).each do |index|
    if digits_sequence[index] == digits_sequence[(index + num_digits / 2) % num_digits]
      sum += digits_sequence[index].to_i
    end
  end 
  return sum
end

def solve_part_one(digits_sequence)
  solve_captcha(digits_sequence)
end

def solve_part_two(digits_sequence)
  solve_captcha_half(digits_sequence)
end

def main
  if File.exist?(INPUT_FILE_NAME)
    digits_sequence = get_digits_sequence(INPUT_FILE_NAME)
    puts "Part One: #{solve_part_one(digits_sequence)}"
    puts "Part Two: #{solve_part_two(digits_sequence)}"
  end 
end

main