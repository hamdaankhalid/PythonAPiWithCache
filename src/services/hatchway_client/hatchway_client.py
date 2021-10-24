import requests

class HatchwayClient:
    HATCHWAY_URL = "https://api.hatchways.io/assessment/blog/posts"

    def __init__(self, communicator, cache):
        self._communicator = communicator
        self._cache = cache

    def get_posts(self, tags, sort_key='id', direction=True):
        res = []
        for tag in tags:
            posts = self._fetch_post(tag)
            for post in posts:
                if post not in res:
                    res.append(post)
        if len(res)>0:
            self._sort_and_arrange(res, sort_key, direction)
        return res
    
    def _sort_and_arrange(self, posts, sort_key, direction):
        posts.sort(key=lambda x: x[sort_key], reverse=direction)

    def _fetch_post(self, tag):
        response = self._communicator.fetch_post(tag, self._cache)
        return response
