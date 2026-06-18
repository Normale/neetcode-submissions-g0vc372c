class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        dims_y, dims_x = len(grid), len(grid[0])
        result = 0

        visited = set()
        def dfs(x, y):
            if (x,y) in visited:
                return
            if not (0 <= x < dims_x):
                return
            if not (0 <= y < dims_y):
                return
            
            visited.add((x,y))
            for dx, dy in [(-1,0), (1,0), (0,1), (0,-1)]:
                dfs(dx, dy)
        
        for x in range(dims_x):
            for y in range(dims_y):
                if grid[y][x] == "1" and (x,y) not in visited:
                    result += 1
                    dfs(x,y)
        return result