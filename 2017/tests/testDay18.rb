require "minitest/autorun"
require_relative "../day18.rb"

TEST_FILE_NAME = "./inputs/day18testinput.txt"

class Day18Test < Minitest::Test
  def test_solve_part_one
    test_registers, test_instructions = get_registers_and_instructions(TEST_FILE_NAME)
    assert_equal(solve_part_one(test_registers, test_instructions), 4)
  end
end