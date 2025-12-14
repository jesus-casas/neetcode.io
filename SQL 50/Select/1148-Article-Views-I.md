2025-12-14

[Leetcode Link](https://leetcode.com/problems/article-views-i/description/?envType=study-plan-v2&envId=top-sql-50)

Tags: [[SQL]]

TC: O(n)
## Code Solution: 

```sql
SELECT 
    DISTINCT author_id AS id 
FROM 
    Views 
WHERE 
    author_id = viewer_id 
ORDER BY 
    id;
```

## Notes:
- AS to rename column
- DISTINCT to remove duplicates
- ORDER BY to sort

