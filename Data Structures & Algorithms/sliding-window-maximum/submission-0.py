from queue import PriorityQueue
from typing import List

class MaxPriorityQueue:
    def __init__(self):
        self.pq = PriorityQueue()

    def push(self, el):
        # Insert element with negative priority to mimic a max heap
        self.pq.put((-el, el))

    def pop(self):
        if not self.pq.empty():
            # Remove and return the element with the highest priority
            return self.pq.get()[1]
        return None

    def peek(self):
        if self.pq.empty():
            return None
        # Peek at the top element by temporarily removing it
        item = self.pq.get()
        self.pq.put(item)
        return item[1]

    def items(self):
        # Retrieve all items for debugging without modifying the queue
        items = []
        result = []
        while not self.pq.empty():
            item = self.pq.get()
            result.append(item[1])
            items.append(item)
        for item in items:
            self.pq.put(item)
        return result

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        pq = MaxPriorityQueue()
        ret = []

        for i in range(k):
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1
            pq.push(nums[i])

        l = 0
        for r in range(k, len(nums) + 1):

            while pq.peek() not in hashmap or hashmap[pq.peek()] == 0:
                pq.pop()
            ret.append(pq.peek())

            hashmap[nums[l]] -= 1
            if hashmap[nums[l]] == 0:
                del hashmap[nums[l]]
            l += 1

            if r < len(nums):
                hashmap[nums[r]] = hashmap.get(nums[r], 0) + 1
                pq.push(nums[r])

        return ret
