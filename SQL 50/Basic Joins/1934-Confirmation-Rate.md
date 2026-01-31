2026-01-26

[Leetcode Link](https://leetcode.com/problems/confirmation-rate/description/?envType=study-plan-v2&envId=top-sql-50)

Tags: [[SQL]]

TC: 
## Code Solution: 

```sql
SELECT s.user_id, round(avg(if(c.action="confirmed",1,0)),2) as confirmation_rate
FROM Signups as s 
LEFT JOIN Confirmations as c
ON s.user_id = c.user_id 
GROUP BY user_id;
```

## Notes:
- 
