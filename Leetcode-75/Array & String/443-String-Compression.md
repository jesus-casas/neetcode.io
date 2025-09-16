2025-08-28

[Leetcode Link](https://leetcode.com/problems/string-compression/description/?envType=study-plan-v2&envId=leetcode-75)

Tags: [[Array & String]] - [[Look Back]] - [[Dry Run]]

TC: O(n)

SC: O(1)

## Code Solution: 

```python
class Solution:
  def compress(self, chars: List[str]) -> int:
    ans = 0
    i = 0

    while i < len(chars):
      letter = chars[i]
      count = 0
      while i < len(chars) and chars[i] == letter:
        count += 1
        i += 1
      chars[ans] = letter
      ans += 1
      if count > 1:
        for c in str(count):
          chars[ans] = c
          ans += 1

    return ans
```

## Notes:
- 
