2025-09-29

[Leetcode Link](https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=leetcode-75)

Tags: [[Two Pointer]]

TC: O(n)

SC: O(1)
## Code Solution: 

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i , j = 0 , len(height)-1
        maxarea = 0
        
        while i < j:
            distance = j - i
            area = min(height[i],height[j]) * distance
            maxarea = max(maxarea, area)
            
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return maxarea
```

## Notes:
- 
