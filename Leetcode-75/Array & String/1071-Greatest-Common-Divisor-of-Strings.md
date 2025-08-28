2024-09-02

[Leetcode Link](https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75)

Tags: [[Array & String]] - [[gcd]]

## Code Solution: 

```python
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if str1 + str2 != str2 + str1:
            return ""
        return str1[:gcd(len(str1), len(str2))]
```

## Notes:
- check if str1 + str2 is the same as the inverse if this is true then that means there is a gcd between str1 and str2 
- so if the case the comparison is not the same we return empty string meaning there is no gcd between our strings
- Finally return str1 from index 0 to the gcd() function of str1 or str2 
