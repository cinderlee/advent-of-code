require "minitest/autorun"
require_relative "../day08.rb"

TEST_FILE_NAME = "./inputs/day08testinput.txt"

class Day08Test < Minitest::Test
  def test_solve
    test_instructions, test_registers = get_program_instructions(TEST_FILE_NAME)

    assert_equal(1, solve_part_one(test_instructions, test_registers))

    test_registers.keys.each { |k| test_registers[k] = 0 }
    assert_equal(10, solve_part_two(test_instructions, test_registers))
  end
end