# Day 21: Fractal Art

INPUT_FILE_NAME = "./inputs/day21input.txt"

INITIAL_PATTERN = [
  [".", "#", "."],
  [".", ".", "#"],
  ["#", "#", "#"]
]

# Returns enhancement rule mappings to convert a pattern to another pattern.
# Each pattern is written as rows top-down separated by slashes. 
def get_rules(file_nm)
  rules = {}
  File.open(file_nm).each do |line|
    rule_key, rule_value = line.chomp.split(" => ")
    rules[rule_key] = rule_value
  end

  rules
end

# Returns the output pattern from flipping the input pattern sideways
def flip(pattern)
  flipped_pattern = []
  pattern.each { |row| flipped_pattern << row.reverse }
  flipped_pattern
end

# Returns list of patterns from rotating input pattern at 90, 180 (flipped vertically), 270 and 360 degrees
def rotate(pattern)
  size = pattern.length
  rotated_pattern = []
  (0...size).each do |col_num|
    row = []
    (0...size).each { |row_num| row << pattern[row_num][col_num] }
    rotated_pattern << row.reverse
  end
  
  rotated_pattern
end

# Returns list of pattern variations from flipping and rotating input pattern
def generate_variations(pattern)
  rotated_patterns = []
  base = pattern
  4.times do
    new_pattern = rotate(base)
    rotated_patterns << new_pattern
    base = new_pattern
  end

  flipped_patterns = rotated_patterns.map { |pattern| flip(pattern) }

  flipped_patterns + rotated_patterns
end

# Generates the next enhanced pattern with empty rows given the current pattern size
# If the current pattern size is divisble by 2, then the next enhanced pattern will have (size / 2) * 3 rows
# Otherwise, the pattern size is divisible by 3. Next pattern will have (size / 3 * 4) rows
def generate_empty_pattern(pattern_size)
  new_pattern = []
  if (pattern_size % 2 == 0)
    new_pattern_rows = pattern_size / 2 * 3
    new_pattern_rows.times { new_pattern << [] }
  else
    new_pattern_rows = pattern_size / 3 * 4
    new_pattern_rows.times { new_pattern << [] }
  end

  new_pattern
end

# Converts a pattern to its string format (rows separated by slashes)
def convert_to_string(pattern)
  pattern.map { |row| row.join("") }.join("/")
end

# Generates the output pattern after running n number of enhancements. 
# If the pattern size is divisble by 2, the pixels will be broken up in 2x2 squares and
# converted into 3x3 using the corresponding enhancement rule.
# Otherwise the pattern size is divisible by 3 and the pixels wil be broken up into 3x3 squares and converted
# into 4x4 using corresponding enhancement rule.
def generate_fractal_art(rules, num_enhancements)
  pattern = INITIAL_PATTERN

  num_enhancements.times do 
    size = pattern.length
    new_pattern = generate_empty_pattern(size)

    step_num = size % 2 == 0 ? 2 : 3
    (0...size).step(step_num).each do |row|
      (0...size).step(step_num).each do |col|
        sub_pattern = (0...step_num).to_a.map { |num| pattern[row + num][col, step_num] }

        sub_pattern_variations = generate_variations(sub_pattern)
        sub_pattern_variations.each do |variation|
          string_representation = convert_to_string(variation)
          if rules.include?(string_representation)
            enhanced_pattern = rules[string_representation].split('/').map { |enhanced_row| enhanced_row.split('')}
            enhanced_size = enhanced_pattern.length
            enhanced_pattern.each_with_index do |new_row, index|
              new_pattern[(row / step_num) * enhanced_size + index].push(*new_row)
            end
            break
          end
        end
      end
    end

    pattern = new_pattern
  end
  
  pattern
end

def get_num_pixels_on(pattern)
  pattern.map { |row| row.join("").count("#") }.sum
end

def solve_part_one(rules)
  enhanced_pattern = generate_fractal_art(rules, 5)
  get_num_pixels_on(enhanced_pattern)
end

def solve_part_two(rules)
  enhanced_pattern = generate_fractal_art(rules, 18)
  get_num_pixels_on(enhanced_pattern)
end

def main
  rules = get_rules(INPUT_FILE_NAME)
  puts "Part One: #{solve_part_one(rules)}"
  puts "Part Two: #{solve_part_two(rules)}"
end

if __FILE__==$0
  main
end