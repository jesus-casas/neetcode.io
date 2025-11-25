# 215-Shopping-Cart-Discount-Calculator

2025-08-03

[Leetcode Link](https://leetcode.com/problems/shopping-cart-discount-calculator/)

Tags: [[Array & String]]

TC: O(n)
## Code Solution: 

```javascript
function solve(items) {
  // Step 1: Compute initial total
  let total = 0;
  for (const [price, quantity] of cart) {
    total += price * quantity;
  }

  // Case 1: total > $100
  let totalAfterPercentage = initialTotal;
  if (total > 100) {
    totalAfterPercentage *= 0.9;
  }

  // Case 2: $20 discount if total >= $200
  let totalAfterFlat = totalAfterPercentage;
  if (totalAfterPercentage >= 200) {
    totalAfterFlat -= 20;
  }

  // Case 3: buy-2-get-1-free discount
  let freeDiscount = 0;
  for (const [price, quantity] of items) {
    if (quantity >= 3) {
      const freeItems = Math.floor(quantity / 3);
      freeDiscount += freeItems * price;
    }
  }

  // Calculate final total
  let finalTotal = totalAfterFlat - freeDiscount;

  // Return a nonnegative total
  return Math.max(finalTotal, 0);
}
```

## Notes:
- 
