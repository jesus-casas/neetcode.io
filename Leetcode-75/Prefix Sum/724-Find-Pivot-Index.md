2025-11-24
[Leetcode Link](https://leetcode.com/problems/find-pivot-index/description)

Tags: [[Prefix Sum]]

TC: O(n)

SC: O(1)

## Code Solution: 

```python
class Solution(object):
    def pivotIndex(self, nums):
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1
```

## Notes:
- 
