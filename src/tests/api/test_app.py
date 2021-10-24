import unittest
import json
from unittest.mock import patch

from src.app import app
from src.services.hatchway_client.hatchway_client_strategy import HatchwayClientStrategy


class RoutesTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.hc = HatchwayClientStrategy.getClient("fake")

    def test_ping(self):
        response = self.app.get(
            '/api/ping', headers={"Content-Type": "application/json"})

        self.assertEqual('true', response.json['success'])
        self.assertEqual(200, response.status_code)

    @patch('src.app.hc.get_posts')
    def test_get_post_success(self, mock):
        mock.return_value = HatchwayClientStrategy.getClient(
            "fake").get_posts(tags=["tech", "health"])
        response = self.app.get('/api/posts',
                                headers={"Content-Type": "application/json"},
                                query_string=dict(tags=('tech', 'health'))
                                )
        self.assertEqual(200, response.status_code)

    def test_get_post_missing_tags(self):
        response = self.app.get(
            '/api/posts', headers={"Content-Type": "application/json"})

        self.assertEqual("Tags parameter is required", response.json['error'])
        self.assertEqual(400, response.status_code)

    def test_get_post_invalid_sortby(self):
        response = self.app.get('/api/posts', headers={"Content-Type": "application/json"},
                                query_string=dict(tags='food', sortBy='Horses'))

        self.assertEqual("sortBy parameter is required",
                         response.json['error'])
        self.assertEqual(400, response.status_code)

    def test_get_post_invalid_direction(self):
        response = self.app.get('/api/posts', headers={"Content-Type": "application/json"},
                                query_string=dict(tags='food', direction='Genies'))

        self.assertEqual("direction parameter is required",
                         response.json['error'])
        self.assertEqual(400, response.status_code)
