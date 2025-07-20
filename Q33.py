# Time Based Key-Value Store
# Implement a time-based key-value data structure that supports:

# Storing multiple values for the same key at specified time stamps
# Retrieving the key's value at a specified timestamp
# Implement the TimeMap class:

# TimeMap() Initializes the object.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns the most recent value of key if set was previously called on it and the most recent timestamp for that key prev_timestamp is less than or equal to the given timestamp (prev_timestamp <= timestamp). If there are no values, it returns "".
# Note: For all calls to set, the timestamps are in strictly increasing order.

from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        items = self.store[key]
        
        left, right = 0, len(items) - 1
        res = ""

        while left <= right:
            mid = (left + right) // 2
            if items[mid][0] <= timestamp:
                res = items[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return res