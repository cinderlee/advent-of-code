# Day 5: A Maze of Twisty Trampolines, All Alike

INPUT_FILE_NAME = "./inputs/day05input.txt"

# Reads a file and returns a list of offsets for each jump
def get_jump_instructions(file_nm)
  offsets = []
  File.open(file_nm).each do |line|
    offsets << line.chomp.to_i
  end
  return offsets
end

# Returns the number of steps it takes for the interrupt to 
# navigate the maze of jump instructions and reach the exit

# After each jump instruction, the offset of the instruction
# increases by 1.
def get_num_steps_part_one(jump_instructions)
  instructions = jump_instructions.slice(0...jump_instructions.length)
  step = 0
  index = 0
  while index < instructions.length
    offset = instructions[index]
    instructions[index] = offset + 1
    index += offset
    step += 1
  end
  return step
end

# Returns the number of steps it takes for the interrupt to 
# navigate the maze of jump instructions and reach the exit

# After each jump instruction, if the offset is at least 3, 
# the offset of the instruction decreases by 1, otherwise it
# increases by 1.
def get_num_steps_part_two(jump_instructions)
  instructions = jump_instructions.slice(0...jump_instructions.length)
  step = 0
  index = 0
  while index < instructions.length
    offset = instructions[index]
    instructions[index] = offset >= 3 ? offset - 1 : offset + 1
    index += offset
    step += 1
  end
  return step
end

def solve_part_one(arr)
  get_num_steps_part_one(arr)
end

def solve_part_two(arr)
  get_num_steps_part_two(arr)
end

def main
  jump_instructions = get_jump_instructions(INPUT_FILE_NAME)
  puts "Part One: #{solve_part_one(jump_instructions)}"
  puts "Part Two: #{solve_part_two(jump_instructions)}"
end

if __FILE__==$0
  main
end