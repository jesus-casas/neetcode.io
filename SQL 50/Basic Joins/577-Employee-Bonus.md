2026-01-01

[Leetcode Link](https://leetcode.com/problems/employee-bonus/description/?envType=study-plan-v2&envId=top-sql-50)

Tags: [[SQL]]

TC:
## Code Solution: 

```sql
SELECT e.name, b.bonus
FROM Employee AS e 
LEFT OUTER JOIN
Bonus AS b ON e.empid = b.empid
WHERE bonus < 1000 OR bonus is NULL;
```

## Notes:
- 
