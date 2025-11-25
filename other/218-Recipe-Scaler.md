2025-09-07

[Leetle Link](https://leetle.app/?date=2025-08-06)

Tags: [[Array & String]]

TC: O(n)

## Code Solution: 

```javascript
function solve(ingredients, scale) {
  const answer = []
  for(const [amount,unit] of ingredients){
    answer.push([amount * scale,unit])
  }
  return answer;
}
```

## Notes:
- 
