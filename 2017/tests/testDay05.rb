require "minitest/autorun"
require_relative "../day05.rb"

TEST_INPUT = [0, 3, 0, 1, -3]

class Day05Test < Minitest::Test
  def test_solve_part_one
    assert_equal(5, solve_part_one(TEST_INPUT))
  end

  def test_solve_part_two
    assert_equal(10, solve_part_two(TEST_INPUT))
  end
end