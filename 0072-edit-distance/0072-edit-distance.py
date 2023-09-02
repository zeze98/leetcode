class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        answer = 0
        m, n = len(word1)+1, len(word2) + 1
        grid = [[0]*n for _ in range(m)]
        
        for y in range(m):
            for x in range(n):
                if y == 0 and x == 0:
                    continue
                elif y == 0:
                    grid[y][x] = x
                elif x == 0:
                    grid[y][x] = y
                else:
                    if word1[y-1] == word2[x-1]: 
                        grid[y][x] = grid[y-1][x-1]
                    else: 
                        grid[y][x] = min(grid[y-1][x-1] + 1, grid[y-1][x] + 1, grid[y][x-1] + 1)
    
        
        return grid[m-1][n-1]