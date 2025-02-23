require "minitest/autorun"
require_relative "../day12.rb"

TEST_INPUT = {
  0 => [2],
  1 => [1],
  2 => [0, 3, 4],
  3 => [2, 4],
  4 => [2, 3, 6],
  5 => [6],
  6 => [4, 5]
}

class Day12Test < Minitest::Test
  def test_solve_part_one
    assert_equal(solve_part_one(TEST_INPUT), 6)
  end

  def test_solve_part_two
    assert_equal(solve_part_two(TEST_INPUT), 2)
  end
end