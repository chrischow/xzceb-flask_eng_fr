import unittest
from translator import english_to_french, french_to_english

class TestTranslations(unittest.TestCase):
    
    # English to French tests
    def test_e2f_equal_hello(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    
    def test_e2f_notequal_goodbye(self):
        self.assertNotEqual(english_to_french('Goodbye'), 'Bonjour')
    
    def test_e2f_none(self):
        self.assertIsNone(english_to_french(None))

    # French to English tests
    def test_f2e_equal_hello(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
    
    def test_f2e_notequal_goodbye(self):
        self.assertNotEqual(french_to_english('Bonjour'), 'Goodbye')
    
    def test_f2e_none(self):
        self.assertIsNone(french_to_english(None))

unittest.main()