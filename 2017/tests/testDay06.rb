require "minitest/autorun"
require_relative "../day06.rb"

TEST_MEMORY_BANKS = [0, 2, 7, 0]

class Day06Test < Minitest::Test
  def test_solve
    test_cycle_count, test_cycles_seen_again = solve(TEST_MEMORY_BANKS)
    assert_equal(5, test_cycle_count)
    assert_equal(4, test_cycles_seen_again)
  end
end