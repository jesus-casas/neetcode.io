2026-01-01

[Leetcode Link](https://leetcode.com/problems/determine-if-two-strings-are-close/?envType=study-plan-v2&envId=leetcode-75)

Tags: [[Look Back]]

TC: O(n)

SC: O(1)
## Code Solution: 

```python
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        word1_elem_freq = Counter(word1)
        word2_elem_freq = Counter(word2)

        return set(word1_elem_freq) == set(word2_elem_freq) and sorted(word1_elem_freq.values()) == sorted(word2_elem_freq.values())
        
```

## Notes:
- If word lengths do not match strings can not be considered close together
- Counter to get letter freq
- Use set of word1 and word2 to ensure each word had the same characters (Condition 1)
- Uses sorted and .values() to ensure each word has the same frequency of characters values (Condition 2)
