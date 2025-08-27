2024-09-02

[Leetcode Link](https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75)

Tags: [[Array & String]]

## Code Solution: 

```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        char1 = list(word1)
        char2 = list(word2)
        maxStringLength = max(len(word1), len(word2))
        anskey = ""
        for i in range (maxStringLength):
            if i < len(word1):
                anskey += char1[i]
            if i < len(word2):
                anskey += char2[i]
        return anskey
```

## Notes:
