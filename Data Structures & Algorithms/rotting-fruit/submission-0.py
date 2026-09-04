class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        w = len(grid[0])
        h = len(grid)
        checks = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        freshCount = 0

        for i in range(h):
            for j in range(w): 
                if grid[i][j] == 2: 
                    q.append((i, j))
                
                if grid[i][j] == 1: 
                    freshCount += 1
        
        minutes = 0

        if freshCount == 0: 
            return 0

        while q and freshCount > 0: 
            
            l = len(q)
            minutes += 1

            for i in range(l): 
                p = q.popleft()

                for ch in checks: 

                    r = p[0] + ch[0]
                    c = p[1] + ch[1]

                    if r < h and r >= 0 and c < w and c >= 0: 
                        if grid[r][c] == 1: 
                            q.append((r, c))
                            grid[r][c] = 2
                            freshCount -= 1
        
        if freshCount: 
            return -1
        else:
            return minutes