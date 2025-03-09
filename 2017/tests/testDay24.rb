require "minitest/autorun"
require_relative "../day24.rb"

TEST_FILE_NAME = "./inputs/day24testinput.txt"

class Day24Test < Minitest::Test
  def setup
    @components = get_magenetic_components(TEST_FILE_NAME)
  end

  def test_get_strongest_bridge
    strongest_bridge_strength = solve_part_one(@components)
    assert_equal(31, strongest_bridge_strength)
  end

  def test_get_strongest_and_lonegest_bridge
    strongest_longest_bridge_strength = solve_part_two(@components)
    assert_equal(19, strongest_longest_bridge_strength)
  end
end