require "minitest/autorun"
require_relative "../day19.rb"

TEST_FILE_NAME = "./inputs/day19testinput.txt"

class Day19Test < Minitest::Test
  def test_trace
    routing_diagram = get_routing_diagram(TEST_FILE_NAME)
    characters, steps = trace(routing_diagram)
    assert_equal("ABCDEF", characters.join(""))
    assert_equal(38, steps)
  end
end