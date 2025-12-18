2025-12-17

[Leetcode Link](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/description/?envType=study-plan-v2&envId=top-sql-50)

Tags: [[Basic Joins]]

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
- 