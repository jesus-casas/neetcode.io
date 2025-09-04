# My Neetcode.io & Leetcode 75 Solutions

These are the solutions that I found to be more intuitive and should have at least a time complexity of O(n), and all solutions include a working Python 3 implementation. I am currently working on adding JavaScript and C++ solutions as well.

## Follow along by using my template.md file

Example Problem

2025-08-26

[Leetcode Link](https://leetcode.com/problems/increasing-triplet-subsequence/?source=submission-noac)

Tags: [[Array & String]]

TC: O(n)

## Code Solution: 

```python
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False
```

## Notes:
