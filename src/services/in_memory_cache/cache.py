from src.services.in_memory_cache.doubly_linked_list import DoublyLinkedList

# Picked this up from leetcode problem I solved a while back
class Cache:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._map = {}
        self.head, self.tail = DoublyLinkedList(0,0), DoublyLinkedList(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self._map:
            retrieved = self._map[key]
            self._remove(retrieved)
            self._add(retrieved)
            return retrieved.val
        return -1

    def insert(self, key: int, value: int) -> None:
        if key in self._map:
            self._remove(self._map[key])
        n = DoublyLinkedList(key, value)
        self._add(n)
        self._map[key] = n
        if len(self._map) > self._capacity:
            n = self.head.next
            self._remove(n)
            del self._map[n.key]

    def _remove(self, node):
        previous = node.prev
        next_up = node.next
        previous.next = next_up
        next_up.prev = previous
    
    def _add(self, node):
        real_tail = self.tail.prev
        real_tail.next = node
        self.tail.prev = node
        node.prev = real_tail
        node.next = self.tail