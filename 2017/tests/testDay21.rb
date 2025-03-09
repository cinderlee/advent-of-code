require "minitest/autorun"
require_relative "../day21.rb"

TEST_RULES = {
  "../.#" => "##./#../...",
  ".#./..#/###" => "#..#/..../..../#..#"
}

class Day21Test < Minitest::Test
  def test_generate_fractal_art
    pattern = generate_fractal_art(TEST_RULES, 2)
    num_pixels_on = get_num_pixels_on(pattern)
    assert_equal(12, num_pixels_on)
  end
end