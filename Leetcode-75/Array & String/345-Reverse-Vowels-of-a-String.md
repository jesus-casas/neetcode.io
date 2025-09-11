2025-08-20

[Leetcode Link](https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&envId=leetcode-75)

Tags: [[Array & String]]

TC: O(n)

SC: O(n)

## Code Solution: 

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        word = list(s)
        start = 0
        end = len(s) - 1
        vowels = "aeiouAEIOU"

        while start < end: 
            while start < end and vowels.find(word[start]) == -1:
                start += 1 

            while start < end and vowels.find(word[end]) == -1:
                end -= 1

            word[start], word[end] = word[end], word[start]

            start += 1 
            end -= 1 

        return "".join(word)
```

## Other Solution:
```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("AEIOUaeiou")
        s = list(s)
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] not in vowels:
                left += 1
            elif s[right] not in vowels:
                right -= 1 
            else: 
                temp = s[left]
                s[left] = s[right]
                s[right] = temp
                left += 1 
                right -= 1
        return "".join(s)
```
## Notes:
- 
