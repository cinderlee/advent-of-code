require "minitest/autorun"
require_relative "../day16.rb"

TEST_PROGRAMS = ("a".."e")
TEST_DANCE_MOVES = [
  [ "s", 1 ],
  [ "x", 3, 4 ],
  [ "p", "e", "b" ]
]
TEST_NUM_TIMES = 2

class Day16Test < Minitest::Test
  def setup
    @test_programs = {}
    TEST_PROGRAMS.to_a.each_with_index { | letter, i | @test_programs[letter] = i }
  end

  def test_solve_part_one
    assert_equal(solve_part_one(@test_programs, TEST_DANCE_MOVES), "baedc")
  end
  
  def test_solve_part_two
    assert solve_part_two(@test_programs, TEST_DANCE_MOVES, TEST_NUM_TIMES) == "ceadb"
  end
end