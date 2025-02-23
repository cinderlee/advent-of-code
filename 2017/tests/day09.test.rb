require "minitest/autorun"
require_relative "../day09.rb"

class Day09Test < Minitest::Test
  def test_get_total_groups_score
    assert_equal(1, get_total_groups_score("{}"))
    assert_equal(6, get_total_groups_score("{{{}}}"))
    assert_equal(5, get_total_groups_score("{{},{}}"))
    assert_equal(16, get_total_groups_score("{{{},{},{{}}}}"))
    assert_equal(1, get_total_groups_score("{<a>,<a>,<a>,<a>}"))
    assert_equal(9, get_total_groups_score("{{<ab>},{<ab>},{<ab>},{<ab>}}"))
    assert_equal(9, get_total_groups_score("{{<!!>},{<!!>},{<!!>},{<!!>}}"))
    assert_equal(3, get_total_groups_score("{{<a!>},{<a!>},{<a!>},{<ab>}}"))
  end

  def test_count_garbage_characters
    assert_equal(0, count_garbage_characters("<>"))
    assert_equal(17, count_garbage_characters("<random characters>"))
    assert_equal(3, count_garbage_characters("<<<<>"))
    assert_equal(2, count_garbage_characters("<{!>}>"))
    assert_equal(0, count_garbage_characters("<!!>"))
    assert_equal(0, count_garbage_characters("<!!!>>"))
    assert_equal(10, count_garbage_characters('<{o"i!a,<{i<a>'))
  end
end