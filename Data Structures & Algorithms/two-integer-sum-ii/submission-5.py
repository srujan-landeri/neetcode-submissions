class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        mapper = dict()
        # 2 3 4
        # 6
        # {
        #     2: 0,
        #     3: 1,
        # }

        for ind, num in enumerate(numbers):
            if target - num in mapper.keys():
                return [mapper[target-num] + 1, ind + 1]
            mapper[num] = ind
        
        return [-1,-1]