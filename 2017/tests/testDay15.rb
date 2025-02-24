require "minitest/autorun"
require_relative "../day15.rb"

TEST_GENERATOR_A_START = 65
TEST_GENERATOR_B_START = 8921

TEST_NUM_PAIRS_PART_ONE = 5
TEST_NUM_PAIRS_PART_TWO = 1056

class Day15Test < Minitest::Test
  def test_solve_part_one
    assert_equal(
      solve_part_one(
        TEST_GENERATOR_A_START,
        GENERATOR_A_FACTOR,
        TEST_GENERATOR_B_START,
        GENERATOR_B_FACTOR, 
        DIVISOR,
        TEST_NUM_PAIRS_PART_ONE
       ), 1
    )
  end

  def test_solve_part_two
    assert_equal(
      solve_part_two(
        TEST_GENERATOR_A_START,
        GENERATOR_A_FACTOR,
        TEST_GENERATOR_B_START,
        GENERATOR_B_FACTOR,
        DIVISOR,
        TEST_NUM_PAIRS_PART_ONE
      ), 0
    )
    
    assert_equal(
      solve_part_two(
        TEST_GENERATOR_A_START,
        GENERATOR_A_FACTOR,
        TEST_GENERATOR_B_START,
        GENERATOR_B_FACTOR,
        DIVISOR,
        TEST_NUM_PAIRS_PART_TWO
      ), 1
    )
  end
end