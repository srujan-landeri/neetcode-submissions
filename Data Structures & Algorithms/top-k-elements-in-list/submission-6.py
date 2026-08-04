class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = dict()
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        freq = [0] * (len(nums) + 1)
        for key,v in counter.items():
            if freq[v] == 0:
                freq[v] = []
            freq[v].append(key)

        i = len(freq) - 1
        return_list = []
        while k > 0 and i >= 0:
            if freq[i] != 0:
                return_list.extend(freq[i])
                k -= len(freq[i])
            i -= 1

        return return_list
