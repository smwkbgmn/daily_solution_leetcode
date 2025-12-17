class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        comlen = len(word1) if len(word1) < len(word2) else len(word2)

        result = ""
        for i in range(0, comlen):
            result += word1[i]
            result += word2[i]
        
        result += word2[comlen:] if len(word1) < len(word2) else word1[comlen:]
        return result
