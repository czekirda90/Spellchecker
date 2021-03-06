import unittest

from spell import SpellChecker

class TestSpellChecker(unittest.TestCase):

	def setUp(self):
		self.spellChecker = SpellChecker()
		self.spellChecker.load_words('spell.word')
		
	def test_spell_checker(self):
		self.assertTrue(self.spellChecker.check_word('zygotic'))
		failed_words = self.spellChecker.check_words('zygotic mistasdas elementary')
		self.assertEquals(1, len(failed_words))
		self.assertEquals('mistasdas', failed_words[0])
		self.assertEquals(0, len(self.spellChecker.check_words('our first correct sentence')))
		self.assertEquals(0, len(self.spellChecker.check_words('Our first correct sentence')))
		self.assertEquals(0, len(self.spellChecker.check_words('Our first correct sentence.')))
		failed_words = self.spellChecker.check_words('zygotic mistasdas spelllleeeing elementary')
		self.assertEquals(2, len(failed_words))
		self.assertEquals('mistasdas', failed_words[0])
		self.assertEquals('spelllleeeing', failed_words[1])
		self.assertEqual(0, len(self.spellChecker.check_document('spell.word')))


if __name__ == '__main__':
    unittest.main()
