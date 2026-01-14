2026-01-13

[Leetcode Link](https://leetcode.com/problems/average-time-of-process-per-machine/description/?envType=study-plan-v2&envId=top-sql-50)

Tags: [[SQL]] - [[]]

TC: 

## Code Solution: 

```sql
# Write your MySQL query statement below
SELECT machine_id, ROUND(SUM(CASE WHEN activity_type = 'start' THEN timestamp*-1 ELSE timestamp END)*1.0/(SELECT COUNT(DISTINCT process_id)),3) AS processing_time
FROM 
    Activity
GROUP BY machine_id
```

## Notes:
- use ROUND(num,spaces) to round to # of spaces
- use SUM to add everything in timestamp
- use 1.0 to keep the left side of the division float to keep decimal places
- use SELECT COUNT(DISTINCT id) to get the number of process_ids


