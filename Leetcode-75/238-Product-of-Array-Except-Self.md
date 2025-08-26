2025-08-25

[Leetcode Link](https://leetcode.com/problems/product-of-array-except-self/?envType=study-plan-v2&envId=leetcode-75)

Tags: [[Array & String]]

TC: O(n)
## Code Solution: 

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = 1
        postfix_product = 1
        n = len(nums)

        ans = [0]*n
        for i in range(n):
            ans[i] = prefix_product
            prefix_product *= nums[i]
        # ans = [1,1,2,6]
        for i in range(n-1,-1,-1):
            ans[i] *= postfix_product
            postfix_product *= nums[i]
        # Dry run
        # 6 *= 1 = 1
        # 2 *= 4 = 8
        # 1 *= 12 = 12
        # 1 *= 24 = 24
        # ans = [24,12,8,1]
        return ans
```

## Notes:
- Calculate the product of the prefix and suffix 
