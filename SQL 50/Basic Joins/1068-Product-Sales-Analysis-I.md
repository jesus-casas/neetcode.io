2025-12-16

[Leetcode Link](https://leetcode.com/problems/product-sales-analysis-i/description/?envType=study-plan-v2&envId=top-sql-50)

Tags: [[Basic Joins]]

TC: 
## Code Solution: 

```sql
SELECT product_name, year, price
FROM Sales
JOIN Product
ON Sales.product_id = Product.product_id
```

## Natural Join Solution:

```sql
SELECT product_name, year, price
FROM Sales
NATURAL JOIN Product
```

## Notes:
- JOIN operation is used to combine data from both tables based on the product_id column.
- ON Sales.product_id = Product.product_id to match the product_id column in both tables.
- NATURAL JOIN is a type of join that automatically matches columns with the same name in both tables.
