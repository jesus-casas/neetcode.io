2025-12-03

[Leetcode Link](https://leetcode.com/problems/unique-number-of-occurrences/description/?envType=study-plan-v2&envId=leetcode-75)

Tags: [[Hash Map & Set]]

TC: O(n)

SC: O(n)

## Code Solution: 

```python
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        
        # Check if all frequency values are unique
        freq_set = set(freq.values())
        
        return len(freq) == len(freq_set)

```

## Notes:
- 
