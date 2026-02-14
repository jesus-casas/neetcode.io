2026-02-13

[Leetcode Link](https://leetcode.com/problems/project-employees-i/?envType=study-plan-v2&envId=top-sql-50)

Tags: [[SQL]]

TC: 
## Code Solution: 

```sql
SELECT
    p.project_id,
    ROUND(AVG(e.experience_years), 2) AS average_years
FROM
    Project AS p
LEFT JOIN
    Employee AS e
ON
    p.employee_id = e.employee_id
GROUP BY
    p.project_id;
```

## Notes:
- 
