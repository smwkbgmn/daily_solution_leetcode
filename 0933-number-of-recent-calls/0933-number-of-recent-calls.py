class RecentCounter:

    def __init__(self):
        self._rec = deque()

    def ping(self, t: int) -> int:
        self._rec.append(t)
        return self._count(t)

    def _count(self, t: int) -> int:
        while self._rec[0] < t - 3000:
            self._rec.popleft()
        return len(self._rec)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)