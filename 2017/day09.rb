# Day 9: Stream Processing

require 'test/unit/assertions'

include Test::Unit::Assertions

INPUT_FILE_NAME = "./inputs/day09input.txt"

# Reads a file and returns a stream of characters. 
def get_character_stream(file_nm)
  stream = nil
  File.open(file_nm) do |file|
    stream = file.first.chomp
  end
  return stream
end

# Return the total score for all groups in the character stream. 

# A group starts with { and ends with }. 
# Garbage starts with < and ends with >. Anything inside the garbage has no meaning.
# The ! character is used to cancel the character that follows directly after it.

# A group's score is 1 more than the parent group score. Outermost group 
# has score of 1. 
def get_total_groups_score(characters)
  group_levels = [0]
  level = 0
  i = 0
  garbage = false
  while i < characters.length
    if characters[i] == "!"
      i += 2
      next
    elsif characters[i] == "<" && !garbage
      garbage = true
    elsif characters[i] == ">"
      garbage = false
    elsif !garbage
      if characters[i] == "{"
        level += 1
      elsif characters[i] == "}" && level > 0
        group_levels[level] = group_levels[level].nil? ? 1 : group_levels[level] + 1
        level -= 1
      end
    end
    i += 1
  end

  cumulative_score = 0
  group_levels.each_with_index { |num, i| cumulative_score += num * i}
  cumulative_score
end

# Return the total number of non-canceled garbage characters.
  
# Garbage starts with < and ends with >. Anything inside the garbage has no meaning.
# The ! character is used to cancel the character that follows directly after it.
def count_garbage_characters(characters)
  i = 0
  is_garbage = false
  garbage_character_count = 0
  while i < characters.length
    if characters[i] == "!"
      i += 2
      next
    elsif characters[i] == "<" && !is_garbage
      is_garbage = true
    elsif characters[i] == ">"
      is_garbage = false
    elsif is_garbage
      garbage_character_count += 1
    end
    i += 1
  end

  garbage_character_count
end

def solve_part_one(characters)
  get_total_groups_score(characters)
end

def solve_part_two(characters)
  count_garbage_characters(characters)
end

def main
  if File.exists?(INPUT_FILE_NAME)
    characters = get_character_stream(INPUT_FILE_NAME)
    puts "Part One: #{solve_part_one(characters)}"
    puts "Part Two: #{solve_part_two(characters)}"
  end
end

main