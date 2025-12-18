2025-12-17

[Leetcode Link](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/description/?envType=study-plan-v2&envId=top-sql-50)

Tags: [[Basic Joins]] - [[Look Back]]

TC: 
## Code Solution: 

```sql
SELECT 
    customer_id, 
    COUNT(visit_id) AS count_no_trans
FROM 
    Visits
WHERE 
    visit_id NOT IN (
        SELECT
            visit_id
        FROM
            Transactions
    )
GROUP BY
    customer_id
```

## Notes:
- COUNT(column) counts the number of non-null values in the specified column.
- GROUP BY groups the rows that have the same values in specified columns into aggregated data.
- NOT IN returns true if the value of a column does not exist in a list of values or subquery results.