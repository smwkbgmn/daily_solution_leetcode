class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        
        if len(t) == 0:
            return False

        if len(s) == 1 and len(t) == 1:
            return s == t

        table = [[0] * 26 for _ in range(len(t) + 1)]
        for i, c in enumerate(t):
            char_i = ord(c) - ord('a')
            for j in reversed(range(i + 1)):
                if table[j][char_i] != 0:
                    break
                table[j][char_i] = i + 1

        # for i in range(0, len(t)):
        #     for j in range(26):
        #         print(table[i][j], end=", ")
        #     print()

        prev = 0
        for c in s:
            char_i = ord(c) - ord('a')
            print(table[prev][char_i])
            if table[prev][char_i] <= prev:
                return False
            prev = table[prev][char_i]
        return True 