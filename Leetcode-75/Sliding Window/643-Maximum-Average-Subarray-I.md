2025-10-09

[Leetcode Link](https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=study-plan-v2&envId=leetcode-75)

Tags: [[Sliding Window]] - [[Look Back]]

TC: O(N)

SC: O(1)

## Code Solution: 

```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        currSum = maxSum = sum(nums[:k])

        for i in range(k,len(nums)):
            # 2 += 50 - 1
            currSum += nums[i] - nums[i - k]

            maxSum = max(maxSum, currSum) # max (2,51)

        return maxSum / k      
```

## Notes:
- 
