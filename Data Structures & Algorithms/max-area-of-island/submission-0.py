class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        dims_y, dims_x = len(grid), len(grid[0])
        visited = set()

        def dfs(x, y, depth):
            if (x,y) in visited:
                return
            if not (0 <= x < dims_x):
                return
            if not (0 <= y < dims_y):
                return
            if grid[y][x] != "1":
                return

            deltas = [(-1,0), (1,0), (0,1), (0,-1)]
            depth += 1
            if depth > max_area:
                max_area = depth
            for dx, dy in deltas:
                dfs(x+dx, y+dy, depth)

        for y in range(dims_y):
            for x in range(dims_x):
                dfs(x,y, 0)

        return max_area