require "minitest/autorun"
require_relative "../day01.rb"

class Day01Test < Minitest::Test
  def test_solve_captcha
    assert_equal(3, solve_captcha("1122"))
    assert_equal(4, solve_captcha("1111"))
    assert_equal(0, solve_captcha("1234"))
    assert_equal(9, solve_captcha("91212129"))
  end

  def test_solve_captcha_half
    assert_equal(6, solve_captcha_half("1212"))
    assert_equal(0, solve_captcha_half("1221"))
    assert_equal(4, solve_captcha_half("123425"))
    assert_equal(12, solve_captcha_half("123123"))
    assert_equal(4, solve_captcha_half("12131415"))
  end
end