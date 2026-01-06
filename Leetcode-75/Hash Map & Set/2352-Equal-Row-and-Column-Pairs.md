2026-01-05

[Leetcode Link](https://leetcode.com/problems/equal-row-and-column-pairs/description/?envType=study-plan-v2&envId=leetcode-75)

Tags: [[Hash Map / Set]]

TC: 

SC:

## Code Solution Optimal: 

```python

```

TC: O(n^3)

SC: O(1)

## Code Solution Brute Force: 

```python
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        n = len(grid)
        
        for r in range(n):
            for c in range(n):
                match = True 

                for i in range(n):
                    if grid[r][i] != grid[i][c]:
                        match = False
                        break
                count += int(match)
        return count
```

## Notes:
- 
