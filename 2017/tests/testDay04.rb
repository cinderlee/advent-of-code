require "minitest/autorun"
require_relative "../day04.rb"

TEST_PASSPHRASE_1 = ["aa", "bb", "cc", "dd", "ee"]
TEST_PASSPHRASE_2 = ["aa", "bb", "cc", "dd", "aa"]
TEST_PASSPHRASE_3 = ["aa", "bb", "cc", "dd", "aaa"]
TEST_PASSPHRASE_4 = ["abcde", "fghij"]
TEST_PASSPHRASE_5 = ["abcde", "xyz", "ecdab"]
TEST_PASSPHRASE_6 = ["a", "ab", "abc", "abd", "abf", "abj"]
TEST_PASSPHRASE_7 = ["iiii", "oiii", "ooii", "oooi", "oooo"]
TEST_PASSPHRASE_8 = ["oiii", "ioii", "iioi", "iiio"]

class Day04Test < Minitest::Test
  def test_is_valid_passphrase_no_repeats
    assert_equal(true, is_valid_passphrase_no_repeats(TEST_PASSPHRASE_1))
    assert_equal(false, is_valid_passphrase_no_repeats(TEST_PASSPHRASE_2))
    assert_equal(true, is_valid_passphrase_no_repeats(TEST_PASSPHRASE_3))
  end

  def test_is_valid_passphrase_no_anagrams
    assert_equal(true, is_valid_passphrase_no_anagrams(TEST_PASSPHRASE_4))
    assert_equal(false, is_valid_passphrase_no_anagrams(TEST_PASSPHRASE_5))
    assert_equal(true, is_valid_passphrase_no_anagrams(TEST_PASSPHRASE_6))
    assert_equal(true, is_valid_passphrase_no_anagrams(TEST_PASSPHRASE_7))
    assert_equal(false, is_valid_passphrase_no_anagrams(TEST_PASSPHRASE_8))
  end
end