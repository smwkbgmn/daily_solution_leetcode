class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_table = [
            "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
        ]

        result = []
        def dfs(i, comb):
            if i == len(digits):
                result.append(comb)
                return

            for letter in letter_table[int(digits[i])]:
                dfs(i + 1, comb + letter)
        dfs(0, "")

        return result