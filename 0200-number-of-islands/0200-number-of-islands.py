class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        answer = 0
        m, n = len(grid), len(grid[0])
        
        def dfs(y, x):
            if x <= -1 or x>=n or y <= -1 or y >= m:
                return False
            if grid[y][x] == '1':
                grid[y][x] = 0
                dfs(y-1, x)
                dfs(y+1, x)
                dfs(y, x-1)
                dfs(y, x+1)
                return True
            return False
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j) == True:
                    answer += 1
   
        return answer