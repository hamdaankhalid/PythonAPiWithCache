import unittest

from src.services.in_memory_cache.cache import Cache

class CacheTest(unittest.TestCase):
    def setUp(self):
        self.cache = Cache(3)
    
    def test_get(self):
        # retreiving item when not in cach returns -1
        non_existent = self.cache.get("I Dont Exist")
        assert non_existent == -1
        # now retreiving a real val
        self.cache.insert('req', 'res')
        valid_return = self.cache.get('req')
        assert valid_return == 'res'

    def test_insert_over_capacity(self):
        self.cache.insert('req1', 'res1')
        self.cache.insert('req2', 'res2')
        self.cache.insert('req3', 'res3')
        retrieved_gets = [self.cache.get('req1'), self.cache.get('req2'), self.cache.get('req3')]
        for retrieved in retrieved_gets:
            assert retrieved != -1
        # add 3 more
        self.cache.insert('req4', 'res1')
        self.cache.insert('req5', 'res2')
        self.cache.insert('req6', 'res3')
        retrieved_gets = [self.cache.get('req1'), self.cache.get('req2'), self.cache.get('req3')]
        for retrieved in retrieved_gets:
            assert retrieved == -1
