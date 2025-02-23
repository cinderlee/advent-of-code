# Day 16: Permutation Promenade

INPUT_FILE_NAME = "./inputs/day16input.txt"
PROGRAMS = ("a".."p")
NUM_TIMES = 1000000000

# Reads a file and returns an array of dance moves
# Each move is represented as a sub-array where the first element represents the move
# and the elements after are the move arguments
def get_dance_moves(file_nm)
  dance_moves = []
  File.open(file_nm) do |file|
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

# Shifts the programs from the end to the front by a number of steps
def spin(programs, number)
  programs.keys.each do |program|
    position = programs[program]
    programs[program] = (position + number) % programs.length
  end
end

# Swaps the programs at location_one and location_two
def exchange(programs, location_one, location_two)
  program_one = nil
  program_two = nil
  programs.each do |program, pos| 
    program_one = program if pos == location_one
    program_two = program if pos == location_two
    break unless program_one.nil? || program_two.nil?
  end

  programs[program_one], programs[program_two] = programs[program_two], programs[program_one]
end

# Swaps the places of program_one and program_two
def partner(programs, program_one, program_two)
  programs[program_one], programs[program_two] = programs[program_two], programs[program_one]
end 

# Performs the dance moves on the list of programs 
def dance(programs, dance_moves)
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

# Returns the final order of the programs in a string 
def get_final_position(programs)
  final_placement = []
  programs.each { |program, pos| final_placement[pos] = program }
  return final_placement.join("")
end

# Returns the final placement of the programs after performing the dance moves
def solve_part_one(programs, dance_moves)
  dance(programs, dance_moves)
  get_final_position(programs)
end

# Returns the final placement of the programs after performing
# the dance moves x amount of times 
def solve_part_two(programs, dance_moves, num_times)
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
  programs = {} 
  PROGRAMS.to_a.each_with_index { | letter, i | programs[letter] = i }
  dance_moves = get_dance_moves(INPUT_FILE_NAME)

  puts "Part One: #{solve_part_one(programs, dance_moves)}"

  # Reset
  PROGRAMS.to_a.each_with_index { | letter, i | programs[letter] = i }
  puts "Part Two: #{solve_part_two(programs, dance_moves, NUM_TIMES)}"
end

if __FILE__==$0
  main
end