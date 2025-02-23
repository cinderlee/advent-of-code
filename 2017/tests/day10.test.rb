require "minitest/autorun"
require_relative "../day10.rb"

NUM_ROUNDS_PART_TWO = 64

TEST_VALUES = [0, 1, 2, 3, 4]
TEST_LENGTHS = [3, 4, 1, 5]

TEST_LENGTHS_INPUT_1 = ""
TEST_LENGTHS_INPUT_2 = "AoC 2017"
TEST_LENGTHS_INPUT_3 = "1,2,3"
TEST_LENGTHS_INPUT_4 = "1,2,4"

class Day10Test < Minitest::Test
  def test_perform_knot_hash
    perform_knot_hash(TEST_VALUES, TEST_LENGTHS)
    assert_equal(TEST_VALUES, [3, 4, 2, 1, 0])
  end

  def test_solve_part_two
    assert_equal(solve_part_two(TEST_LENGTHS_INPUT_1, NUM_ROUNDS_PART_TWO), "a2582a3a0e66e6e86e3812dcb672a272")
    assert_equal(solve_part_two(TEST_LENGTHS_INPUT_2, NUM_ROUNDS_PART_TWO), "33efeb34ea91902bb2f59c9920caa6cd")
    assert_equal(solve_part_two(TEST_LENGTHS_INPUT_3, NUM_ROUNDS_PART_TWO), "3efbe78a8d82f29979031a4aa0b16a9d")
    assert_equal(solve_part_two(TEST_LENGTHS_INPUT_4, NUM_ROUNDS_PART_TWO), "63960835bcdc130f0b66d7ff4f6a5a8e")
  end
end