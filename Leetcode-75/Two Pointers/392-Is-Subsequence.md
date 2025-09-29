2025-09-28

[Leetcode Link](https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=leetcode-75)

Tags: [[Two Pointers]]

TC: O(n)

SC: O(1)

## Code Solution: 

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
```

## Notes:
- 
