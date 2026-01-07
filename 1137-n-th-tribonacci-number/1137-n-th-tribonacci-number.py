class Solution:
    def tribonacci(self, n: int) -> int:
        tri = [0, 1, 1]
        
        if n < 3:
            return tri[n]
        
        total = 2
        for i in range(3, n):
            tri[0], tri[1], tri[2], total = tri[1], tri[2], total, total - tri[0] + total

        return total