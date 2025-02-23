# Day 23: Coprocessor Conflagration

INPUT_FILE_NAME = "./inputs/day23input.txt"

VALID_REGISTER_NAMES = ("a".."h")

# Determines whether the specified value is a valid register name (a to h)
def is_register?(value)
  VALID_REGISTER_NAMES.include?(value)
end

# Reads a file and returns a mapping of register -> values and list of instructions
def get_registers_and_instructions(file_nm)
  registers = {}
  instructions = []
  File.open(file_nm).each do |line|
    instr = line.chomp.split(" ")
    (1...instr.length).each do |index|
      if (is_register?(instr[index]))
        registers[instr[index]] = 0
      else
        instr[index] = instr[index].to_i
      end
    end
    instructions << instr
  end

  return registers, instructions
end

# Returns value depending on whether the argument is register name or purely a number
def get_argument_value(argument, registers)
  is_register?(argument) ? registers[argument] : argument
end

# Run a set of instructions with existing register mapping. Returns the number
# of times the mul instruction has been executed 

# Instructions
# - set x y: sets register X to value of Y
# - sub x y: decrements value of register X by Y
# - mul x y: sets register x to the product of x and y
# - jnz x y: jumps to next step y away only if x is not 0
def solve_part_one(registers, instructions)  
  pos = 0
  mul_times = 0
  while pos >= 0 && pos < instructions.length
    step = 1
    instr = instructions[pos]
    instr_name = instr[0]
    arg_one = instr[1]
    arg_two = instr.length == 3 ? get_argument_value(instr[2], registers) : 0

    case instr_name
    when "set"
      registers[arg_one] = arg_two
    when "sub"
      registers[arg_one] -= arg_two
    when "mul"
      registers[arg_one] *= arg_two
      mul_times += 1
    when "jnz"
      step = arg_two if get_argument_value(arg_one, registers) != 0
    end
    pos += step
  end
  mul_times
end

# Run a set of instructions with existing register mapping. The logic below is 
# the translated logic of the assembly language instructions where register 'a' begins
# with a value of 1

# Returns the value stored in register 'h'
def solve_part_two
  registers = {
    b: 93,
    c: 93,
    d: 0, 
    e: 0,
    f: 0,
    g: 1,  # set to non-zero to start the loop
    h: 0
  }

  # when a is not 0, the logic below is applied
  registers[:b] = registers[:b] * 100 + 100_000
  registers[:c] = registers[:b] + 17_000

  until registers[:g] == 0
    registers[:f] = 1
    registers[:d] = 2

    # condensed version of the assembly code 
    # for d = 2 -> b
    #   for e = 2 -> b
    #      f = 0 if e * d == b 
    # for every number pairing of (d, e) whose product is b, f will be set to 0
    # logic below breaks early the moment the first pairing is discovered
    while registers[:d] < registers[:b]
      if registers[:b] % registers[:d] == 0
        registers[:f] = 0
        break
      end
      registers[:d] += 1
    end

    registers[:h] += 1 if registers[:f] == 0
    registers[:g] = registers[:b] - registers[:c]
    registers[:b] += 17
  end

  registers[:h]
end 

def main
  registers, instructions = get_registers_and_instructions(INPUT_FILE_NAME)
  puts "Part One: #{solve_part_one(registers, instructions)}"
  puts "Part Two: #{solve_part_two}"
end

main