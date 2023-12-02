import json
from typing import Tuple
import os

cachePath = os.path.dirname(os.path.realpath(__file__)) + "/.cache"


class Cache:
    def __init__(self, values: dict):
        self.values = values

    def loadValue(self, value: int) -> Tuple[int, int] | False:
        if value not in self.values:
            return False
        return self.values[value]

    def saveValue(self, value: int, result: Tuple[int, int]) -> None:
        if not isinstance(result, tuple):
            raise TypeError("Result is not a tuple")
        if not len(result) == 2:
            raise ValueError("Result must have two values")
        self.values[value] = result

    def saveCache(self) -> None:
        with open(cachePath, "w") as cache:
            json.dump(self.values, cache, indent=4, sort_keys=True)


def loadCache() -> Cache:
    try:
        with open(cachePath, "r") as cache:
            return Cache(json.load(cache))
    except FileNotFoundError:
        with open(cachePath, "w") as cache:
            json.dump(dict(), cache)
        return loadCache()
