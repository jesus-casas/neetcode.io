2025-12-13

[Leetcode Link](https://leetcode.com/problems/find-customer-referee/?envType=study-plan-v2&envId=top-sql-50)

Tags: [[SQL]]

TC: O(n)
## Code Solution: 

```sql
SELECT name
FROM Customer
WHERE referee_id != 2 OR referee_id IS NULL;
```

## Notes:
- 
