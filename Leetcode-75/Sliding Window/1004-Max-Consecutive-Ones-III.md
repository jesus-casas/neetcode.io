2025-10-15

[Leetcode Link](https://leetcode.com/problems/max-consecutive-ones-iii/description/?envType=study-plan-v2&envId=leetcode-75)

Tags: [[Sliding Window]] - [[Look Back]]

TC: O(N)

SC: O(1)
## Code Solution: 

```python
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = max_consec = 0

        for right, num in enumerate(nums):
            k -= 1 - num # 1 - 0 or 1 - 1

            if k < 0:
                k += 1 - nums[left]
                left += 1
            else:
                max_consec = max(max_consec, right - left + 1)

        return max_consec
```

## Notes:
- 
