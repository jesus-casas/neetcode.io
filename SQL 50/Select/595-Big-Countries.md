2025-12-14

[Leetcode Link](https://leetcode.com/problems/big-countries/?envType=study-plan-v2&envId=top-sql-50)

Tags: [[SQL]]

TC: O(n)
## Code Solution: 

```sql
SELECT name, population, area
FROM World
WHERE area >= 3000000 or population >= 25000000;
```

## Notes:
- 
