require "minitest/autorun"
require_relative "../day14.rb"

TEST_INPUT_KEY = "flqrgnkx"

class Day14Test < Minitest::Test
  def test_solve
    test_num_used_squares, test_num_regions = solve(TEST_INPUT_KEY)
    assert_equal(test_num_used_squares, 8108)
    assert_equal(test_num_regions, 1242)
  end
end