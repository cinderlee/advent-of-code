# Day 7: Recursive Circus

INPUT_FILE_NAME = "./inputs/day07input.txt"

# Reads a file and returns information about the tower of programs
# including their weights, sub towers, and sub towers cumulative weights
def get_tower_of_programs(file_nm)
  programs = {}
  sub_tower_weights = {}
  File.open(file_nm).each do |line|
    line_parts = line.chomp.split(" ")
    program_name = line_parts[0]
    weight = line_parts[1].chomp(")")[1..].to_i
    sub_tower = []
    if (line_parts.find_index("->").nil?)
      sub_tower_weights[program_name] = weight
    else
      sub_tower_index_start = line_parts.find_index("->") + 1
      sub_tower_index_end = line_parts.length - 1
      (sub_tower_index_start..sub_tower_index_end).each do |index|
        sub_tower << line_parts[index].chomp(",")
      end
      programs[program_name] = {
        :sub_tower => sub_tower,
        :weight => weight
      }
    end
  end
  [ programs, sub_tower_weights ]
end

# Returns the program name at the bottom of the tower. In this tower structure,
# there is one program holding up subtowers. 
def get_bottom_program(programs)
  complete_sub_tower_list = []
  programs.each do |program, program_info|
    sub_tower = program_info[:sub_tower]
    sub_tower.each { |sub_program| complete_sub_tower_list << sub_program } unless sub_tower == []
  end

  # There should be one program not in the sub tower list, and that
  # would bethe bottom program
  (programs.keys - complete_sub_tower_list)[0]
end

# Calculates and stores the cumulative weight of the sub tower
# located at the the current program.
def populate_sub_tower_weights(curr_program, programs, sub_tower_weights)
  total = programs[curr_program][:weight]
  sub_tower = programs[curr_program][:sub_tower]
  sub_tower.each do |program_name|
    populate_sub_tower_weights(program_name, programs, sub_tower_weights) if sub_tower_weights[program_name].nil?
    total += sub_tower_weights[program_name]
  end
  sub_tower_weights[curr_program] = total
end

# Return the correct weight for the program that has the incorrect weight
# leading to an imbalance for the whole towere

# Each subtower should have the same cumulative weight and only one program
# has the incorrect weight
def get_correct_weight(bottom_program, programs, sub_tower_weights)
  curr_program = bottom_program
  correct_sub_tower_weight = 0
  populate_sub_tower_weights(curr_program, programs, sub_tower_weights)

  while true
    sub_tower = programs[curr_program][:sub_tower]
    weights = sub_tower.map { |program_name| sub_tower_weights[program_name] }
    incorect_weight_index = weights.find_index(weights.select { |w| weights.count(w) == 1 }[0])

    # if all the weights in the sub tower are the same 
    # then the current program has the incorrect weight
    return correct_sub_tower_weight - weights.sum if (incorect_weight_index.nil?)
    # otherwise look at the next sub tower child that has incorrect cumulative weight
    curr_program = sub_tower[incorect_weight_index]
    correct_sub_tower_weight = weights.select { |w| weights.count(w) == weights.length - 1}[0]
  end
end

def solve_part_one(programs)
  get_bottom_program(programs)
end

def solve_part_two(programs, sub_tower_weights)
  bottom_program = get_bottom_program(programs)
  get_correct_weight(bottom_program, programs, sub_tower_weights)
end

def main
  if File.exist?(INPUT_FILE_NAME)
    programs, sub_tower_weights = get_tower_of_programs(INPUT_FILE_NAME)
    puts "Part One: #{solve_part_one(programs)}"
    puts "Part Two: #{solve_part_two(programs, sub_tower_weights)}"
  end
end

main