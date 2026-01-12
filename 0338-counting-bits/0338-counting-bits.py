class Solution:
    def countBits(self, n: int) -> List[int]:
        table = [0, 1, 1, 2]
        if n < 4:
            return table[:n+1]

        m = 4
        while m <= n:
            for i in range(m):
                table.append(table[i] + 1)
                if len(table) == n + 1:
                    break
            m *= 2
        
        return table