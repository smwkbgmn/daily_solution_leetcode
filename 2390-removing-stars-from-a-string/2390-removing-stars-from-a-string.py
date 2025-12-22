class Solution:
    def removeStars(self, s: str) -> str:
        rst_list = []
        for c in s:
            if c == '*':
                rst_list.pop()
            else:
                rst_list.append(c)
        return ''.join(rst_list)