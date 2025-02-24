require "minitest/autorun"
require_relative "../day08.rb"

TEST_FILE_NAME = "./inputs/day08testinput.txt"

class Day08Test < Minitest::Test
  def setup
    @test_instructions, @test_registers = get_program_instructions(TEST_FILE_NAME)
  end

  def test_solve_part_one
    assert_equal(1, solve_part_one(@test_instructions, @test_registers))
  end

  def test_solve_part_two
    assert_equal(10, solve_part_two(@test_instructions, @test_registers))
  end
end