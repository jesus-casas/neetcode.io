2026-01-21

[Leetcode Link](https://leetcode.com/problems/managers-with-at-least-5-direct-reports/?envType=study-plan-v2&envId=top-sql-50)

Tags: [[SQL]]

TC: 
## Code Solution: 

```sql
# Write your MySQL query statement below
SELECT 
    name 
FROM 
    Employee AS t1
JOIN
    (SELECT
        ManagerId
    From
        Employee
    GROUP BY ManagerId
    HAVING COUNT(ManagerId) >= 5) AS t2
ON 
    t1.Id = t2.managerId
```

## Notes:
- HAVING clause filters out the managerId having a count of reports greater than or equal to 5.
- t1.Id = t2.ManagerId keeps rows where an employee’s Id matches one of the ManagerIds from the subquery
