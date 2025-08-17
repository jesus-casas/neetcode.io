2025-08-17
[Leetcode Link](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/?envType=study-plan-v2&envId=leetcode-75)

Tags: [[Array & String]]

TC: O(n)
## Code Solution: 

```python
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        maxCandies = max(candies)
        for candie in candies:
            if (candie + extraCandies) >= maxCandies:
                ans.append(True)
            else:
                ans.append(False)
        return ans
```

## Notes:
- 
