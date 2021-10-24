from src.services.hatchway_client.hatchway_client import HatchwayClient
from src.services.hatchway_client.real_communicator import RealCommunicator
from src.services.hatchway_client.fake_communicator import FakeCommunicator
from src.services.in_memory_cache.cache import Cache


class HatchwayClientStrategy:
    
    HATCHWAY_API_CACHE_CAP = 1000

    @staticmethod
    def getClient(strategy):
        if strategy == "real":
            communicator = RealCommunicator()
        else:
            communicator = FakeCommunicator()

        cache = Cache(HatchwayClientStrategy.HATCHWAY_API_CACHE_CAP)
        return HatchwayClient(communicator, cache)
