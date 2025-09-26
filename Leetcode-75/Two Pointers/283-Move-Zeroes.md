
2025-09-25

[Leetcode Link](https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75)

Tags: [[Two Pointers]]

TC: O(n)

SC: O(1)

## Code Solution: 

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l] #swap in python
                l += 1
        return nums
```

## Notes:
- 1 is truthy
- 0 is falsy
