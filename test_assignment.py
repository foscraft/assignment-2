import unittest
from urllib import response

import requests
from json_dict import to_json,jsons_response
from guess import perfect_guess, random_number
from perfect_square import perfect_square
from power_of_four import power_of_four
from simple_statistics import statss
# from timeout import timeOutResponse

class TestAssignment(unittest.TestCase):

    def test_random_number(self):
        self.assertIsInstance(random_number(0,5),int)

    def test_perfect_guess(self):
        self.assertEqual(perfect_guess(),"This is higher. Please try again.")
        self.assertEqual(perfect_guess(),"This is lower. Please try again.")
        self.assertEqual(perfect_guess(),"This is not a valid integer. Please try again")

    def test_json_dict(self):
        self.assertTrue(to_json(jsons_response('https://api.openalex.org/authors'))['meta'],
                type(to_json(jsons_response('https://api.openalex.org/authors'))['meta'])==dict)

    def test_jsons_dict(self):
        resp = requests.get('https://api.openalex.org/authors')
        self.assertEqual(resp.status_code, 200)

    def test_perfect_square(self):
        self.assertTrue(perfect_square(81))
        self.assertTrue(perfect_square(625))
        self.assertFalse(perfect_square(243))

    def test_power_of_four(self):
        self.assertTrue(power_of_four(16))
        self.assertFalse(power_of_four(15))

    def test_simple_stats(self):
        self.assertEqual(statss([56,44,5,6,6,7,8,99,34,56,3232]),
                        {'minimum value': 5, 'maximum_value': 3232, 'average': 323, 'median value': 34})

    def test_timeout(self):
        pass

    def test_web_response(self):
        resp = requests.get('https://api.openalex.org/authors?per-page=100&page=1')
        self.assertEqual(resp.status_code,200)


if __name__ == '__main__':
    unittest.main()