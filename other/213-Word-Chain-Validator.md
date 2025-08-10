2025-08-09
[Leetle Link]()
Tags: [[Array & String]]
TC: 
## Code Solution: 

```javascript
function solve(words) {
    if (words.length <= 1) return true;
    for (let i = 0; i < words.length - 1; i++) {
        const currentLast = words[i].slice(-1).toLowerCase();
        const nextFirst = words[i + 1][0].toLowerCase();
        if (currentLast !== nextFirst) {
            return false;
        }
    }
    return true;
}
```

## Notes:
- 
