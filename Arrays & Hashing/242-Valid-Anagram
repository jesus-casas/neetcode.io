2024-09-02
[Leetcode Link](https://leetcode.com/problems/valid-anagram/description/)
Tags: [[Array & String]]
TC: O(n)
## Code Solution: 

```javascript
if (s.length != t.length){return false}

const counts = {};

for(let c of s){
	counts[c] = (counts[c] || 0) + 1;
}

for (let c of t){
	if (!counts[c]) return false;
	counts[c]--;
}

return true;
```

## Notes:
- 
