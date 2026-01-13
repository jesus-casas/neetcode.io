2025-01-12

[Leetcode Link](https://leetcode.com/problems/rising-temperature/description/?envType=study-plan-v2&envId=top-sql-50)

Tags: [[Basic Joins]] - [[Look Back]]

TC: 
## Code Solution: 

```sql
SELECT 
    w1.id
FROM 
    Weather w1
JOIN 
    Weather w2
ON 
    DATEDIFF(w1.recordDate, w2.recordDate) = 1
WHERE 
    w1.temperature > w2.temperature;
```

## Notes:
- DATEDIFF calculate the difference between two dates or timestamps and return the result as an integer in a specified unit of timestamps
