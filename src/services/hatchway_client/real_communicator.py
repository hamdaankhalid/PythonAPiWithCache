import requests

class RealCommunicator:
    HATCHWAY_URL = "https://api.hatchways.io/assessment/blog/posts"

    def fetch_post(self, tag, cache):
        PARAMS = {'tag':tag}
        retrieved = cache.get(tag)
        if retrieved == -1:
            response = requests.get(self.HATCHWAY_URL, params = PARAMS).json()
            return response['posts']
        return retrieved['posts']