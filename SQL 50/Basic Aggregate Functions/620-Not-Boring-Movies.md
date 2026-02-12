2026-02-11

[Leetcode Link](https://leetcode.com/problems/not-boring-movies/description/?envType=study-plan-v2&envId=top-sql-50)

Tags: [[SQL]]

TC: 
## Code Solution: 

```sql
select *
from cinema
where mod(id, 2) = 1 and description != 'boring'
order by rating DESC;
```

## Notes:
- 
