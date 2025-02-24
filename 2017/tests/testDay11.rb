require "minitest/autorun"
require_relative "../day11.rb"

TEST_STEPS_1 = ["ne", "ne", "ne"]
TEST_STEPS_2 = ["ne", "ne", "sw", "sw"]
TEST_STEPS_3 = ["ne", "ne", "s", "s"]
TEST_STEPS_4 = ["se", "sw", "se", "sw", "sw"]

class Day11Test < Minitest::Test
  def test_solve_part_one
    assert_equal(solve_part_one(TEST_STEPS_1), 3)
    assert_equal(solve_part_one(TEST_STEPS_2), 0)
    assert_equal(solve_part_one(TEST_STEPS_3), 2)
    assert_equal(solve_part_one(TEST_STEPS_4), 3)
  end
end