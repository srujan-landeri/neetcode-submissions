from queue import PriorityQueue

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = dict()
        return_list = []
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        pq = PriorityQueue()
        for key,v in counter.items():
            pq.put((-v,key))

        for i in range(k):
            occurences, number = pq.get()
            return_list.append(number)
    
        return return_list