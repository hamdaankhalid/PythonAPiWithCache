import unittest
import json

from src.services.hatchway_client.hatchway_client_strategy import HatchwayClientStrategy
from src.tests.services.expected_api_data import expected_ascending_popularity_sort_result, expected_descending_id_sort_result

class RoutesTest(unittest.TestCase):

    def setUp(self):
        self.hc = HatchwayClientStrategy.getClient('real')
    
    def test_get_posts_sort_asc(self):
        resp = self.hc.get_posts(tags=['science','health'], sort_key='popularity')
        assert resp == expected_ascending_popularity_sort_result
 
    def test_get_posts_sort_desc(self):
        resp = self.hc.get_posts(tags=['science','health'], sort_key='id',direction=False)
        assert resp == expected_descending_id_sort_result
    
