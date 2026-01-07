class Solution:
    def tribonacci(self, n: int) -> int:
        tri = deque([0, 1, 1])
        
        if n < 3:
            return tri[n]
        
        total = 2
        for i in range(3, n):
            tri.append(total)
            total += total
            total -= tri[0]
            tri.popleft()

        return total