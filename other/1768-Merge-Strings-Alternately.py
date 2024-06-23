class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        char1 = list(word1)
        char2 = list(word2)
        anskey = ""
        max_length = max(len(char1), len(char2))
        for i in range(max_length):
            if i < len(char1):
                anskey += char1[i]
            if i < len(char2):
                anskey += char2[i]
        return anskey