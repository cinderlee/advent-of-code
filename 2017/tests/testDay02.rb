require "minitest/autorun"
require_relative "../day02.rb"

TEST_INPUT = [
  [5, 1, 9, 5],
  [7, 5, 3],
  [2, 4, 6, 8]
]

TEST_INPUT_2 = [
  [5, 9, 2, 8],
  [9, 4, 7, 3],
  [3, 8, 6, 5]
]

class Day02Test < Minitest::Test
  def test_solve_part_one
    assert_equal(18, solve_part_one(TEST_INPUT))
  end

  def test_solve_part_two
    assert_equal(9, solve_part_two(TEST_INPUT_2))
  end
end