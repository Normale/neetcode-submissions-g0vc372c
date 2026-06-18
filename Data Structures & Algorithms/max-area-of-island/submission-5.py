class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        dims_y, dims_x = len(grid), len(grid[0])
        visited = set()

        def dfs(x, y):
            if (x,y) in visited:
                return 0
            if not (0 <= x < dims_x):
                return 0
            if not (0 <= y < dims_y):
                return 0
            if grid[y][x] != 1:
                return 0

            deltas = [(-1,0), (1,0), (0,1), (0,-1)]
            visited.add((x,y))

            for dx, dy in deltas:
                area += dfs(x+dx, y+dy)
            return area
        
        max_area = 0
        for y in range(dims_y):
            for x in range(dims_x):
                max_area = max(dfs(x,y), max_area)

        return max_area