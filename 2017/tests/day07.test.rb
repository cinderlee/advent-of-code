require "minitest/autorun"
require_relative "../day07.rb"

TEST_FILE_NAME = "./inputs/day07testinput.txt"

class Day07Test < Minitest::Test
  def test_solve
    test_programs, test_sub_tower_weights = get_tower_of_programs(TEST_FILE_NAME)
    assert_equal("tknk", solve_part_one(test_programs))
    assert_equal(60, solve_part_two(test_programs, test_sub_tower_weights))
  end
end