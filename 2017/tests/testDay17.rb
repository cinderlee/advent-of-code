require "minitest/autorun"
require_relative "../day17.rb"

class Day17Test < Minitest::Test
  def test_solve_part_one
    assert_equal(solve_part_one(PART_ONE_NUM_TIMES, 3), 638)
  end
end