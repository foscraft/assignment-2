import unittest
# from json_dict import jsonsResponse
# from perfect_guess import perfectGuess
from perfect_square import perfectSquare
from power_of_four import powerOfFour
# from simple_statistics import statss
# from timeout import timeOutResponse
# from web_page_r import webPageResponse

class TestAssignment(unittest.TestCase):

    def test_perfect_guess(self):
        pass

    def test_perfect_square(self):
        self.assertTrue(perfectSquare(81))
        self.assertTrue(perfectSquare(625))
        self.assertFalse(perfectSquare(243))

    def test_power_of_four(self):
        self.assertTrue(powerOfFour(16))
        self.assertFalse(powerOfFour(15))

    def test_json_dict(self):
        pass

    def test_simple_stats(self):
        pass

    def test_timeout(self):
        pass

    def test_web_response(self):
        pass


if __name__ == '__main__':
    unittest.main()