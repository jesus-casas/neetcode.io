2025-08-21

[Leetcode Link](https://leetcode.com/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=leetcode-75)

Tags: [[Array & String]]

TC: O(n)

SC: O(n)

## Code Solution: 
### Python solution using .join(), .split(), and reversed()
```python
class Solution:
	def reverseWords(self, s: str) -> str:
		return " ".join(reversed(s.split()))
```


## ALT Solution:

[::-1] creates a new list in reverse order so its better to use reversed() in big s cases
```python
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
```

## Notes:
- 
