2025-10-12

[Leetcode Link](https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=study-plan-v2&envId=leetcode-75)

Tags: [[Array & String]]

TC: O(n)

SC: O(1)

## Code Solution: 

```python
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        currVowel = 0
        maxVowel = 0

        # Count vowels in the first window
        for i in range(k):
            if s[i] in vowels:
                currVowel += 1
        maxVowel = currVowel

        # Slide the window
        for i in range(k, len(s)):
            if s[i] in vowels:
                currVowel += 1
            if s[i - k] in vowels:
                currVowel -= 1
            maxVowel = max(maxVowel, currVowel)

        return maxVowel

```

## Notes:
- use a set for constant lookup time
