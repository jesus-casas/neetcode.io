class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,n in enumerate(nums):
            complement = target - n 
            if complement in hashmap:
                return [i,hashmap[complement]]
            hashmap[n] = i