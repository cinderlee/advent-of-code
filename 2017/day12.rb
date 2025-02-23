# Day 12: Digital Plumber

INPUT_FILE_NAME = "./inputs/day12input.txt"

# Reads a file and returns a hash map of the list of program ids
# each program can communicate directly to. The communication
# is bidirectional.
def get_program_links(file_nm)
  programs = {}
  File.open(file_nm).each do |line|
    communication = line.chomp.split(" ")
    program_id = communication[0].to_i
    connected_to_list = communication.slice(2..).map { |program_id| program_id.to_i }
    programs[program_id] = connected_to_list
  end
  return programs
end

# Returns the group of program ids that can communicate via pipes 
# indirectly or directly to the starting program id.
def find_group_with_program_id(programs, program_id)
  group = [program_id]
  group.each do |program_id|
    connected_to_list = programs[program_id]
    connected_to_list.each { |connected_id| group << connected_id unless group.include?(connected_id) }
  end
  return group
end

# Returns the number of programs that are in the group that
# contains program id 0
def solve_part_one(programs)
  find_group_with_program_id(programs, 0).length
end

# Returns the total number of groups among the programs that can
# communicate indirectly or directly 
def solve_part_two(programs)
  program_ids = programs.keys
  groups = 0
  until program_ids.empty?
    group = find_group_with_program_id(programs, program_ids[0])
    groups += 1
    program_ids = program_ids - group
  end
  return groups
end

def main
  programs = get_program_links(INPUT_FILE_NAME)
  puts "Part One: #{solve_part_one(programs)}"
  puts "Part Two: #{solve_part_two(programs)}"
end

if __FILE__==$0
  main
end