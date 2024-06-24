class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # if strings are the same we return empty string
        if str1 + str2 != str2 + str1:
            return ""
        # return gcd of both strings
        return str1[:gcd(len(str1), len(str2))]