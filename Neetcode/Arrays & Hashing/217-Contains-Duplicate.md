2024-09-02
[Leetcode Link](https://leetcode.com/problems/contains-duplicate/description/)

Tags: [[Array & String]]

TC: O(n)

SC: O(n)

## Code Solution: 

```python
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set() 
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
```

## Notes:
- 