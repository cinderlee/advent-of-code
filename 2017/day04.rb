# Day 4: High-Entropy Passphrases

INPUT_FILE_NAME = "./inputs/day04input.txt"

# Reads a file and returns the list of passphrases
def get_passphrases(file_nm)
  passphrases = []
  File.open(file_nm).each do |line|
    passphrases << line.chomp.split(" ")
  end
  return passphrases
end

# Returns whether two words are anagrams of each other
def are_anagrams(first_word, second_word)
  return false unless first_word.length == second_word.length
  first_word.each_char { |char| return false unless first_word.count(char) == second_word.count(char) }
  return true
end

# Returns whether a passphrase is valid. A valid passphrase has unique words
def is_valid_passphrase_no_repeats(passphrase)
  passphrase.length == passphrase.uniq.length
end

# Returns whether a passphrase is valid. A valid passphrase contains words 
# that are not anagrams of each other
def is_valid_passphrase_no_anagrams(passphrase)
  (0...passphrase.length).each do |index|
    (index + 1...passphrase.length).each do |other_index|
      return false if are_anagrams(passphrase[index], passphrase[other_index])
    end
  end
  return true
end

# Returns the number of valid passphrases that contain unique words
def count_valid_passphrases_no_repeats(passphrases)
  passphrases.select { |passphrase| is_valid_passphrase_no_repeats(passphrase) }.length
end

# Returns the number of valid passphrases that do not contain anagrams
# This is an addiitonal system policy on top of the previous one of having unique words
def count_valid_passphrases_no_anagrams(passphrases)
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
  if File.exist?(INPUT_FILE_NAME)
    passphrases = get_passphrases(INPUT_FILE_NAME)
    puts "Part One: #{solve_part_one(passphrases)}"
    puts "Part Two: #{solve_part_two(passphrases)}"
  end
end

main