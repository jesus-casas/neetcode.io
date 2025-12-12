2025-09-02

[Leetcode Link](https://leetcode.com/problems/recyclable-and-low-fat-products/description/?envType=study-plan-v2&envId=top-sql-50)

Tags: [[SQL]] - 

TC: 
## Code Solution: 

```sql
SELECT product_id
FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y';
```

## Notes:
- 
