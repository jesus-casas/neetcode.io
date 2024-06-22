class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        hashmap1 = {}
        hashmap2 = {} 
        charS = list(s)
        charT = list(t)
        anskey = 0
        for i, n in enumerate(charS):
            hashmap1[n] = i
        for i, n in enumerate(charT):
            hashmap2[n] = i
        for char in charS:
            anskey += abs(hashmap1[char] - hashmap2[char])

        return anskey
