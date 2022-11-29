"""
Time O(N) Space O(1)
Design a data structure that follows Least Recently Used (LRU) cache.
LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
get(int key) Return the value of the key if the key exists, otherwise return -1.
put(int key, int value) Update the value of the key if the key exists.
Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation,
evict the least recently used key. The functions get and put must each run in O(1) average time complexity.
"""
from collections import deque


class LRUCacheDeQue:

    def __init__(self, capacity):
        self.n = capacity
        self.hash_map = {}
        self.cache = deque()

    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1
        self.cache.remove(key)
        self.cache.appendleft(key)
        return self.hash_map[key]

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            self.cache.remove(key)
        else:
            if self.n == len(self.cache):
                oldest = self.cache.pop()
                del self.hash_map[oldest]
        self.cache.appendleft(key)
        self.hash_map[key] = value


class Node:

    def __init__(self, key=None, value=None):
        self.key, self.value = key, value
        self.prev = self.next = None


class LRUCacheLinkedLIst:

    def __init__(self, capacity: int):
        self.n = capacity
        self.hash_map = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def append_left(self, node: Node) -> None:
        nxt = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = nxt
        nxt.prev = node

    def remove(self, node: Node) -> None:
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1
        node = self.hash_map[key]
        self.remove(node)
        self.append_left(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            node = self.hash_map[key]
            self.remove(node)
            node.value = value
        else:
            if self.n == len(self.hash_map):
                oldest = self.head.prev
                self.remove(oldest)
                del self.hash_map[oldest.key]
            node = Node(key, value)
        self.append_left(node)
        self.hash_map[key] = node





