2025-12-14

[Leetcode Link](https://leetcode.com/problems/invalid-tweets/description/?envType=study-plan-v2&envId=top-sql-50)

Tags: [[SQL]]

TC: O(n)
## Code Solution: 

```sql
SELECT tweet_id
FROM Tweets
WHERE CHAR_LENGTH(content) > 15;
```

## Notes:
- CHAR_LENGTH to get length of string since LENGTH will return the number of bytes