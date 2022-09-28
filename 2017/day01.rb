# Day 1: Inverse Captcha

require 'test/unit/assertions'

include Test::Unit::Assertions

INPUT_FILE_NAME = "./inputs/day01input.txt"

def get_digits_sequence(file_nm)
  # Reads a file and returns the sequence of digits (on the first line)

  sequence = nil
  File.open(INPUT_FILE_NAME) do |file|
    sequence = file.first
  end
  return sequence
end

def solve_captcha(digits_sequence)
  # Solves a captcha by finding the sum of all digits in the sequence
  # that match the next digit. The sequence is circular so the next
  # digit after the last will be the first digit.

  sum = 0
  num_digits = digits_sequence.length
  (0...num_digits).each do |index|
    if digits_sequence[index] == digits_sequence[(index + 1) % num_digits]
      sum += digits_sequence[index].to_i
    end
  end 
  return sum
end

def solve_captcha_half(digits_sequence)
  # Solves a captcha by finding the sum of all digits in the sequence
  # that match the digit halfway around the circular sequence.

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
  assert solve_captcha("1122") == 3
  assert solve_captcha("1111") == 4
  assert solve_captcha("1234") == 0
  assert solve_captcha("91212129") == 9

  assert solve_captcha_half("1212") == 6
  assert solve_captcha_half("1221") == 0
  assert solve_captcha_half("123425") == 4
  assert solve_captcha_half("123123") == 12
  assert solve_captcha_half("12131415") == 4

  digits_sequence = get_digits_sequence(INPUT_FILE_NAME)
  puts "Part One: #{solve_part_one(digits_sequence)}"
  puts "Part Two: #{solve_part_two(digits_sequence)}"
end

main