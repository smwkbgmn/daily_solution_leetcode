class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        check = [False] * len(rooms)

        def traverse(room, i_current):
            check[i_current] = True
            for i in room:
                if check[i] == False and i != i_current:
                    traverse(rooms[i], i)
        traverse(rooms[0], 0)

        return all(check)