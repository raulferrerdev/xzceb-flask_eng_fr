import unittest
from machinetranslation.translator import english_to_french, french_to_english

class TestMyTranslator(unittest.TestCase):

    '''Test for null input for french to english'''
    def test_french_to_english_translate_with_null_input(self):
        input_text = None
        try:
            french_to_english(input_text)
            assert(False, "Function did not raise ValueError for null input")
        except ValueError:
            pass

    '''Test for null input for english to french'''
    def test_english_to_french_translate_with_null_input(self):
        input_text = None
        try:
            english_to_french(input_text)
            assert(False, "Function did not raise ValueError for null input")
        except ValueError:
            pass

    '''Test for translation from french to english'''
    def test_french_to_english_translation(self):
        input_text = 'Bonjour'
        expected_output = 'Hello'
        actual_output = french_to_english(input_text)
        self.assertEqual(actual_output, expected_output, "Translation successful")

    '''Test for null input for english to french'''
    def test_english_to_french_translation(self):
        input_text = 'Hello'
        expected_output = 'Bonjour'
        actual_output = english_to_french(input_text)
        self.assertEqual(actual_output, expected_output, "Translation successful")

if __name__ == '__main__':
    unittest.main()
