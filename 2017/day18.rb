# Day 18: Duet

INPUT_FILE_NAME = "./inputs/day18input.txt"

VALID_REGISTER_NAMES = ("a".."z")

# Determines whether the specified value is a valid register name (a to z)
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

# Run a set of instructions with existing register mapping. Returns the value 
# of the recovered frequency the first time rcv is called with non-zero value 

# Instructions
# - snd x: plays a sound equal to value x
# - set x y: sets register X to value of Y
# - add x y: increments value of register X by Y
# - mul x y: sets register x to the product of x and y
# - mod x y: set register x to the mod of x and y
# - rcv x: recovers the last sound played when x is not 0
# - jgz x y: jumps to next step y away only if x is greater than 0
def solve_part_one(registers, instructions)  
  pos = 0
  last_frequency = nil
  while pos < instructions.length
    step = 1
    instr = instructions[pos]
    instr_name = instr[0]
    arg_one = instr[1]
    arg_two = instr.length == 3 ? get_argument_value(instr[2], registers) : 0

    case instr_name
    when "snd"
      last_frequency = get_argument_value(arg_one, registers)
    when "set"
      registers[arg_one] = arg_two
    when "add"
      registers[arg_one] += arg_two
    when "mul"
      registers[arg_one] *= arg_two
    when "mod"
      registers[arg_one] %= arg_two
    when "rcv"
      return last_frequency if get_argument_value(arg_one, registers) != 0
    when "jgz"
      step = arg_two if get_argument_value(arg_one, registers) > 0
    end
    pos += step
  end
end


class Program 
  attr_reader :is_paused, :is_done
  
  def initialize(registers, instructions)
    @registers = registers
    @instructions = instructions
    @program_position = 0
    @message_queue = []
    @message_queue_position = 0
    @is_paused = false
    @is_done = false
  end

  # Returns number of messages received from another program 
  def get_queue_length
    @message_queue.length
  end

  # Runs the next instruction with existing register mapping. 

  # Instructions
  # - snd x: sends X to the other program (adds to their queue)
  # - set x y: sets register X to value of Y
  # - add x y: increments value of register X by Y
  # - mul x y: sets register x to the product of x and y
  # - mod x y: set register x to the mod of x and y
  # - rcv x: receives next value from the message queue and store in register x
  #        : if next value not found, program is paused and waits for value to be sent
  # - jgz x y: jumps to next step y away only if x is greater than 0
  def run_next_instruction(other_program)
    if @program_position >= @instructions.length
      @is_done = true
      return
    end

    step = 1
    instruction = @instructions[@program_position]
    instruction_name = instruction[0]
    arg_one = instruction[1]
    arg_two = instruction.length == 3 ? get_argument_value(instruction[2]) : 0

    case instruction_name
    when "snd"
      value = get_argument_value(arg_one)
      other_program.receive(value)
    when "set"
      @registers[arg_one] = arg_two
    when "add"
      @registers[arg_one] += arg_two
    when "mul"
      @registers[arg_one] *= arg_two
    when "mod"
      @registers[arg_one] %= arg_two
    when "rcv"
      if @message_queue[@message_queue_position]
        @registers[arg_one] = @message_queue[@message_queue_position]
        @message_queue_position += 1
        @is_paused = false
      else
        @is_paused = true
        return
      end
    when "jgz"
      step = arg_two if get_argument_value(arg_one) > 0
    end
    @program_position += step
  end

  protected

  # Receives the value sent from a different program and adds to message queue
  def receive(value)
    @message_queue << value
  end

  private

  # Returns value depending on whether the argument is register name or purely a number
  def get_argument_value(argument)
    is_register?(argument) ? @registers[argument] : argument
  end
end

# Run two programs in parallel and returns the number of messages program one sent 
# when both have been terminated (due to deadlock -- both waiting to receive next messages)

# Note: Each program's register p starts with value of program id (0, 1)
def solve_part_two(registers_program_zero, registers_program_one, instructions)
  program_zero = Program.new(registers_program_zero, instructions)
  program_one = Program.new(registers_program_one, instructions)
  while true
    program_zero.run_next_instruction(program_one)
    program_one.run_next_instruction(program_zero)
    if (program_zero.is_paused && program_one.is_paused)
      return program_zero.get_queue_length
    end
  end
end

def main
  registers, instructions = get_registers_and_instructions(INPUT_FILE_NAME)
  puts "Part One: #{solve_part_one(registers, instructions)}"

  registers_program_zero = {}
  registers_program_one = {}
  registers.keys.each do |key|
    registers_program_zero[key] = 0
    registers_program_one[key] = 0
  end
  registers_program_one["p"] = 1

  puts "Part Two: #{solve_part_two(registers_program_zero, registers_program_one, instructions)}"
end

if __FILE__==$0
  main
end