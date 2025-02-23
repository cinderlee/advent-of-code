require "minitest/autorun"
require_relative "../day03.rb"

class Day03Test < Minitest::Test
  def test_solve_part_one
    assert_equal(0, solve_part_one(1))
    assert_equal(3, solve_part_one(12))
    assert_equal(2, solve_part_one(23))
    assert_equal(31, solve_part_one(1024))
  end
end