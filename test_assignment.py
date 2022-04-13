import unittest
from urllib import response

import requests
from json_dict import to_json,jsons_response
# from json_dict import jsonsResponse, toJson
# from perfect_guess import perfectGuess
from perfect_square import perfect_square
from power_of_four import power_of_four
from simple_statistics import statss
# from simple_statistics import statss
# from timeout import timeOutResponse
# from web_page_r import webPageResponse

class TestAssignment(unittest.TestCase):

    def test_perfect_guess(self):
        pass

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
        pass


if __name__ == '__main__':
    unittest.main()