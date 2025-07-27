2025-07-21
[Leetcode Link](https://leetcode.com/problems/two-sum/)
Tags: [[Array & String]]
TC: O(n) 

## Code Solution: 

```javascript
const map = {}

for (let i=0;i < nums.length;i++){
	let complement = target - nums[i];
	if (map.hasOwnProperty(complement)){
		return [map[complement],i]
	}
map[nums[i]] = i;
}
return [];
```

```python
hashmap = {} # c:i
	for i,n in enumerate(nums):
		diff = target - n 
		if diff in hashmap:
			return [hashmap[diff], i]
		hashmap[n] = i
	return
```

## Notes:
- Create map
- Find complement
- return indices
