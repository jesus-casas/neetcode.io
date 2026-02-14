2026-01-01

[Leetcode Link](https://leetcode.com/problems/percentage-of-users-attended-a-contest/description/?envType=study-plan-v2&envId=top-sql-50)

Tags: [[SQL]]

TC: 
## Code Solution: 

```sql
# Write your MySQL query statement below
SELECT  
    contest_id,
    ROUND( 
        COUNT(DISTINCT user_id) * 100 / (
            SELECT 
                COUNT(user_id) 
            FROM 
                Users
        ),
        2
    ) AS percentage
    
FROM 
    Register
GROUP BY 
    Contest_id
ORDER BY
    percentage DESC,
    contest_id ASC;
```

## Notes:
- 
