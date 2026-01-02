from collections import deque
from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        height, width = len(maze), len(maze[0])
        
        queue = deque([(entrance[0], entrance[1], 0)]) 
        maze[entrance[0]][entrance[1]] = '+'
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue:
            row, col, steps = queue.popleft()
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                if not (0 <= new_row < height and 0 <= new_col < width):
                    continue
                if maze[new_row][new_col] != '.':
                    continue
                
                is_border = (new_row == 0 or new_row == height - 1 or 
                           new_col == 0 or new_col == width - 1)
                if is_border:
                    return steps + 1
                
                maze[new_row][new_col] = '+'
                queue.append((new_row, new_col, steps + 1))
        
        return -1