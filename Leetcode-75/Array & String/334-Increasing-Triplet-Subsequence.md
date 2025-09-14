2025-08-26

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
