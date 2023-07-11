#2.2
#2.1 Unit Testing
import unittest

from Isogram import isogram_checker

class IsogramTestCase(unittest.TestCase):
    def test_special_characters_not_isogram(self): # Test if a word with special characters is not an isogram
        self.assertFalse(isogram_checker("hello@world"))

    def test_single_word_isogram_checker(self): # Test if single word is an isogram
        self.assertTrue(isogram_checker("isogram"))

    def test_single_word_not_isogram(self): # Test if a single word is not an isogram
        self.assertFalse(isogram_checker("hello"))

    def test_whitespace_isogram_checker(self): # Test if a word with whitespace  is an isogram
        self.assertTrue(isogram_checker("   "))

    def test_empty_string(self): # Test if an empty string an isogram
        self.assertTrue(isogram_checker(""))

    def test_single_character(self): # Test if a single character an isogram
        self.assertTrue(isogram_checker("a"))

    def test_repeated_letters(self): # Test if a word with repeated letters an isogram
        self.assertFalse(isogram_checker("helloo"))

    def test_mixed_case_isogram_checker(self):# Test if a word with mixed case that is an isogram
        self.assertTrue(isogram_checker("UnCoPyRiGhTaBlE"))

    def test_mixed_case_not_isogram(self): # Test if a word with mixed case that is not an isogram
        self.assertFalse(isogram_checker("HeLLo"))



    def test_whitespace_not_isogram(self): # Test if a word with whitespace is not an isogram
        self.assertFalse(isogram_checker("hello world"))

    def test_special_characters_isogram_checker(self): # Test if a word with special characters is an isogram
        self.assertTrue(isogram_checker("@#$%^&*"))

    def test_unicode_isogram_checker(self): # Test if a word with Unicode characters is an isogram
        self.assertTrue(isogram_checker("αβγδε"))
