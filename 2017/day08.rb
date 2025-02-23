# Day 8: I Heard You Like Registers

INPUT_FILE_NAME = "./inputs/day08input.txt"

# Reads a file and returns a list of program instructions and 
# a hash map of registers to their initial values (0)
def get_program_instructions(file_nm)
  instructions = []
  registers = {}
  File.open(file_nm).each do |line|
    instruction = line.chomp.split(" ")

    # locate register names and set to 0
    register_one = instruction[0]
    register_two = instruction[4]
    registers[register_one] = 0
    registers[register_two] = 0

    # convert to numbers
    instruction[2] = instruction[2].to_i
    instruction[-1] = instruction[-1].to_i
    
    instructions << instruction
  end
  return instructions, registers
end

# Returns whether the condition for the instruction is true 
def is_condition_met(condition, registers)
  register = condition[0]
  condition_operator = condition[1]
  val = condition[2]

  case condition_operator
  when ">"
    registers[register] > val
  when ">="
    registers[register] >= val
  when "<"
    registers[register] < val
  when "<="
    registers[register] <= val
  when "=="
    registers[register] == val
  when "!="
    registers[register] != val
  else
    false
  end
end

# Performs the program instruction
def run_instruction(instruction, registers) 
  register = instruction[0]
  operator = instruction[1]
  val = instruction[2]

  case operator
  when "inc"
    registers[register] += val
  when "dec"
    registers[register] -= val
  end
end

# Returns the highest value held in any register while 
# executing the program instructions
def run_instructions(instructions, registers)
  max_value = 0
  instructions.each do |instr|
    valid = nil
    if is_condition_met(instr[-3..], registers)
      run_instruction(instr, registers)
      max_value = registers[instr[0]] if registers[instr[0]] > max_value
    end
  end
  max_value
end

# Returns the number of programs that are in the group that
# contains program id 0
def solve_part_one(instructions, registers)
  run_instructions(instructions, registers)
  registers.values.max
end

# Returns the highest value held in any register during the 
# program execution
def solve_part_two(instructions, registers)
  run_instructions(instructions, registers)
end

def main
  instructions, registers = get_program_instructions(INPUT_FILE_NAME)
  puts "Part One: #{solve_part_one(instructions, registers)}"

  registers.keys.each { |k| registers[k] = 0 }
  puts "Part Two: #{solve_part_two(instructions, registers)}"
end

if __FILE__==$0
  main
end