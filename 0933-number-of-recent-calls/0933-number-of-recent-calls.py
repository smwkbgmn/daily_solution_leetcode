class RecentCounter:

    def __init__(self):
        self._rec = SortedList([])

    def ping(self, t: int) -> int:
        self._rec.add(t)
        return self._count(t)

    def _count(self, t: int) -> int:
        return bisect.bisect_left(self._rec, t) - bisect.bisect_left(self._rec, t - 3000) + 1


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)