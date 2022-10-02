# Day 12: Digital Plumber

require 'test/unit/assertions'

include Test::Unit::Assertions

INPUT_FILE_NAME = "./inputs/day12input.txt"
TEST_INPUT = {
  0 => [2],
  1 => [1],
  2 => [0, 3, 4],
  3 => [2, 4],
  4 => [2, 3, 6],
  5 => [6],
  6 => [4, 5]
}

def get_program_links(file_nm)
  # Reads a file and returns a hash map of the list of program ids
  # each program can communicate directly to. The communication
  # is bidirectional.

  programs = {}
  File.open(INPUT_FILE_NAME).each do |line|
    communication = line.chomp.split(" ")
    program_id = communication[0].to_i
    connected_to_list = communication.slice(2..).map { |program_id| program_id.to_i }
    programs[program_id] = connected_to_list
  end
  return programs
end

def find_group_with_program_id(programs, program_id)
  # Returns the group of program ids that can communicate via pipes 
  # indirectly or directly to the starting program id.

  group = [program_id]
  index = 0 
  while (index < group.length)
    connected_to_list = programs[group[index]]
    connected_to_list.each { |program_id| group.push(program_id) if !group.include?(program_id) }
    index += 1
  end
  return group
end

def solve_part_one(programs)
  # Returns the number of programs that are in the group that
  # contains program id 0

  find_group_with_program_id(programs, 0).length
end

def solve_part_two(programs)
  # Returns the total number of groups among the programs that can
  # communicate indirectly or directly 

  program_ids = programs.keys
  groups = 0
  while (!program_ids.empty?)
    group = find_group_with_program_id(programs, program_ids[0])
    groups += 1
    program_ids = program_ids - group
  end
  return groups
end

def main
  assert solve_part_one(TEST_INPUT) == 6
  assert solve_part_two(TEST_INPUT) == 2

  programs = get_program_links(INPUT_FILE_NAME)
  puts "Part One: #{solve_part_one(programs)}"
  puts "Part Two: #{solve_part_two(programs)}"
end

main