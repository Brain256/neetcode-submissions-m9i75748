class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        islands = 0
        checks = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for i in range(len(grid)): 
            for j in range(len(grid[i])): 
                if grid[i][j] == "0" or grid[i][j] == "2": 
                    continue

                islands += 1

                q = deque([(i, j)])

                while q: 
                    
                    row, col = q.popleft()

                    for c in checks: 
                        newR = row + c[0]
                        newC = col + c[1]

                        if 0 <= newR <= len(grid)-1 and 0 <= newC <= len(grid[0])-1: 
                            if grid[newR][newC] == "1": 
                                q.append((newR, newC))
                                grid[newR][newC] = "2"

        return islands


