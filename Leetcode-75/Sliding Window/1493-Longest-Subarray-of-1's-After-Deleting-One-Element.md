2025-11-22
[Leetcode Link](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/?envType=study-plan-v2&envId=leetcode-75)

Tags: [[Sliding Window]]

TC: O(n)

SC: O(1)

## Code Solution: 

```python
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        zeroCount = 0
        longestWindow = 0
        start = 0

        for i in range(len(nums)):
            # Count zeros as we expand the window
            if nums[i] == 0:
                zeroCount += 1

            # If more than one zero shrink window from the left 
            while zeroCount > 1:
                if nums[start] == 0:
                    zeroCount -= 1
                start += 1

            # Update longest window which is i - start gives window length minus 1
            longestWindow = max(longestWindow, i - start)

        return longestWindow

```

## Notes:
- 
