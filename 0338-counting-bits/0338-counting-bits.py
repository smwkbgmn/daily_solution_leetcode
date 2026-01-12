class Solution:
    def countBits(self, n: int) -> List[int]:
        table = [0, 1, 1, 2]

        m = 4
        while m <= n:
            table.extend([i + 1 for i in table])
            m *= 2
        
        return table[:n + 1]