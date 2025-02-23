require "minitest/autorun"
require_relative "../day13.rb"

TEST_FILE_NAME = "./inputs/day13testinput.txt"

class Day13Test < Minitest::Test
  def setup
    @test_firewall_scanner_range = get_firewall_info(TEST_FILE_NAME)
  end

  def test_solve_part_one
    assert_equal(solve_part_one(@test_firewall_scanner_range), 24)
  end

  def test_solve_part_two
    assert_equal(solve_part_two(@test_firewall_scanner_range), 10)
  end
end