2025-12-14

[Leetcode Link](https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/?envType=study-plan-v2&envId=top-sql-50)

Tags: [[SQL]]

TC: O(n)
## Code Solution: 

```sql
SELECT EmployeeUNI.unique_id, Employees.name
FROM Employees
LEFT JOIN EmployeeUNI
ON Employees.id = EmployeeUNI.id;
```

## Notes:
- SELECT table_name.column_name to select a specific column from a table
- LEFT JOIN operation to combine data from both tables based on the id column.
- ON Employees.id = EmployeeUNI.id to match the id column in both tables.