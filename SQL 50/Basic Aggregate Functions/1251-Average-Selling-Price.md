2026-02-12 

[Leetcode Link](https://leetcode.com/problems/average-selling-price/?envType=study-plan-v2&envId=top-sql-50)

Tags: [[SQL]]

TC: 
## Code Solution: 

```sql
SELECT
    p.product_id,
    IFNULL(ROUND(SUM(p.price * u.units) / SUM(u.units), 2), 0) AS average_price
FROM
    Prices AS p
LEFT JOIN
    UnitsSold AS u
ON
    p.product_id = u.product_id
    AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY
    p.product_id;
```

## Notes:
- IFNULL returns 0 if a product has no sales

