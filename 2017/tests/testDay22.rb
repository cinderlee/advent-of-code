require "minitest/autorun"
require_relative "../day22.rb"

TEST_FILE_NAME = "./inputs/day22testinput.txt"

class Day22Test < Minitest::Test
  def setup
    @nodes_information = get_nodes(TEST_FILE_NAME)
  end

  def test_simulate_bursts
    num_infected = simulate_bursts(10000, @nodes_information)
    assert_equal(5587, num_infected)
  end

  def test_simulate_bursts_evolved
    num_infected = simulate_bursts(10000000, @nodes_information, true)
    assert_equal(2511944, num_infected)
  end
end