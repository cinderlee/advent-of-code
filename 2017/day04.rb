# Day 4: High-Entropy Passphrases

require 'test/unit/assertions'

include Test::Unit::Assertions

INPUT_FILE_NAME = "./inputs/day04input.txt"

TEST_PASSPHRASE_1 = ["aa", "bb", "cc", "dd", "ee"]
TEST_PASSPHRASE_2 = ["aa", "bb", "cc", "dd", "aa"]
TEST_PASSPHRASE_3 = ["aa", "bb", "cc", "dd", "aaa"]
TEST_PASSPHRASE_4 = ["abcde", "fghij"]
TEST_PASSPHRASE_5 = ["abcde", "xyz", "ecdab"]
TEST_PASSPHRASE_6 = ["a", "ab", "abc", "abd", "abf", "abj"]
TEST_PASSPHRASE_7 = ["iiii", "oiii", "ooii", "oooi", "oooo"]
TEST_PASSPHRASE_8 = ["oiii", "ioii", "iioi", "iiio"]

def get_passphrases(file_nm)
  # Reads a file and returns the list of passphrases

  passphrases = []
  File.open(file_nm).each do |line|
    passphrases << line.chomp.split(" ")
  end
  return passphrases
end

def are_anagrams(first_word, second_word)
  # Returns whether two words are anagrams of each other

  return false unless first_word.length == second_word.length
  first_word.each_char { |char| return false unless first_word.count(char) == second_word.count(char) }
  return true
end

def is_valid_passphrase_no_repeats(passphrase)
  # Returns whether a passphrase is valid. A valid passphrase has unique words

  passphrase.each { |word| return false unless passphrase.count(word) == 1 }
  return true
end

def is_valid_passphrase_no_anagrams(passphrase)
  # Returns whether a passphrase is valid. A valid passphrase contains words 
  # that are not anagrams of each other

  (0...passphrase.length).each do |index|
    (index + 1...passphrase.length).each do |other_index|
      return false if are_anagrams(passphrase[index], passphrase[other_index])
    end
  end
  return true
end

def count_valid_passphrases_no_repeats(passphrases)
  # Returns the number of valid passphrases that contain unique words

  passphrases.select { |passphrase| is_valid_passphrase_no_repeats(passphrase) }.length
end

def count_valid_passphrases_no_anagrams(passphrases)
  # Returns the number of valid passphrases that do not contain anagrams
  # This is an addiitonal system policy on top of the previous one of having unique words

  passphrases_no_repeats = passphrases.select { |passphrase| is_valid_passphrase_no_repeats(passphrase) }
  passphrases_no_repeats.select { |passphrase| is_valid_passphrase_no_anagrams(passphrase) }.length
end

def solve_part_one(passphrases)
  count_valid_passphrases_no_repeats(passphrases)
end

def solve_part_two(passphrases)
  count_valid_passphrases_no_anagrams(passphrases)
end

def main
  assert is_valid_passphrase_no_repeats(TEST_PASSPHRASE_1) == true
  assert is_valid_passphrase_no_repeats(TEST_PASSPHRASE_2) == false
  assert is_valid_passphrase_no_repeats(TEST_PASSPHRASE_3) == true

  assert is_valid_passphrase_no_anagrams(TEST_PASSPHRASE_4) == true
  assert is_valid_passphrase_no_anagrams(TEST_PASSPHRASE_5) == false
  assert is_valid_passphrase_no_anagrams(TEST_PASSPHRASE_6) == true
  assert is_valid_passphrase_no_anagrams(TEST_PASSPHRASE_7) == true
  assert is_valid_passphrase_no_anagrams(TEST_PASSPHRASE_8) == false

  passphrases = get_passphrases(INPUT_FILE_NAME)
  puts "Part One: #{solve_part_one(passphrases)}"
  puts "Part Two: #{solve_part_two(passphrases)}"
end

main