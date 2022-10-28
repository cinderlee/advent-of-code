# Day 16: Permutation Promenade

require 'test/unit/assertions'

include Test::Unit::Assertions

INPUT_FILE_NAME = "./inputs/day16input.txt"
PROGRAMS = ("a".."p")
NUM_TIMES = 1000000000

TEST_PROGRAMS = ("a".."e")
TEST_DANCE_MOVES = [
  [ "s", 1 ],
  [ "x", 3, 4 ],
  [ "p", "e", "b" ]
]
TEST_NUM_TIMES = 2

def get_dance_moves(file_nm)
  # Reads a file and returns an array of dance moves
  # Each move is represented as a sub-array where the first element represents the move
  # and the elements after are the move arguments

  dance_moves = []
  File.open(INPUT_FILE_NAME) do |file|
    moves = file.first.chomp.split(",")
    moves.each do |move|
      step = move[0]
      case step
      when "s"
        shift_num = move[1..].to_i
        dance_moves << [step, shift_num]
      when "x"
        positions = move[1..].split('/').map { |pos| pos.to_i }
        dance_moves << [step].concat(positions)
      else
        program_names = move[1..].split('/')
        dance_moves << [step].concat(program_names)
      end
    end
  end
  return dance_moves
end

def spin(programs, number)
  # Shifts the programs from the end to the front by a number of steps
  programs.keys.each do |program|
    position = programs[program]
    programs[program] = (position + number) % programs.length
  end
end

def exchange(programs, location_one, location_two)
  # Swaps the programs at location_one and location_two

  program_one = nil
  program_two = nil
  programs.each do |program, pos| 
    program_one = program if pos == location_one
    program_two = program if pos == location_two
    break unless program_one.nil? || program_two.nil?
  end

  programs[program_one], programs[program_two] = programs[program_two], programs[program_one]
end

def partner(programs, program_one, program_two)
  # Swaps the places of program_one and program_two

  programs[program_one], programs[program_two] = programs[program_two], programs[program_one]
end 

def dance(programs, dance_moves) 
  # Performs the dance moves on the list of programs 

  dance_moves.each do |move|
    step = move[0]
    case step
    when "s"
      spin(programs, move[1])
    when "x"
      exchange(programs, move[1], move[2])
    else
      partner(programs, move[1], move[2])
    end
  end
end

def get_final_position(programs)
  # Returns the final order of the programs in a string 

  final_placement = []
  programs.each { |program, pos| final_placement[pos] = program }
  return final_placement.join("")
end

def solve_part_one(programs, dance_moves)
  # Returns the final placement of the programs after performing 
  # the dance moves
  dance(programs, dance_moves)
  get_final_position(programs)
end

def solve_part_two(programs, dance_moves, num_times)
  # Returns the final placement of the programs after performing
  # the dance moves x amount of times 

  dance_endings = [get_final_position(programs)]
  cycle_count = nil

  num_times.times do
    dance(programs, dance_moves)
    final_pos = get_final_position(programs)
    if (dance_endings.include?(final_pos))
      break
    else
      dance_endings << final_pos
    end
  end 

  leftover = num_times % dance_endings.length
  dance_endings[leftover]
end

def main
  test_programs = {}
  TEST_PROGRAMS.to_a.each_with_index { | letter, i | test_programs[letter] = i }
  assert solve_part_one(test_programs, TEST_DANCE_MOVES) == "baedc"
  TEST_PROGRAMS.to_a.each_with_index { | letter, i | test_programs[letter] = i }
  assert solve_part_two(test_programs, TEST_DANCE_MOVES, TEST_NUM_TIMES) == "ceadb"

  programs = {} 
  PROGRAMS.to_a.each_with_index { | letter, i | programs[letter] = i }
  dance_moves = get_dance_moves(INPUT_FILE_NAME)

  puts "Part One: #{solve_part_one(programs, dance_moves)}"

  # Reset
  PROGRAMS.to_a.each_with_index { | letter, i | programs[letter] = i }
  puts "Part Two: #{solve_part_two(programs, dance_moves, NUM_TIMES)}"
end

main