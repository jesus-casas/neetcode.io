# My Neetcode.io, Leetcode 75, and SQL 50 Solutions

These solutions are the ones I found most intuitive and should have the time complexity of O(n) for each solution. All solutions will include a working Python 3 implementation. I am currently working on adding JavaScript and C++ solutions as well.

## Follow along using template.md and Obsidian

### Example Problem:
334 Increasing Triplet Subsequence

2026-01-01

[Leetcode Link](https://leetcode.com/problems/increasing-triplet-subsequence/?source=submission-noac)

Tags: [[Array & String]]

TC: O(n)

SC: O(1)

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
