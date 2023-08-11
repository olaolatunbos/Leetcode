class Solution:
    def numIslands(self, grid) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        islands = 0

        def traverse(i, j):
            queue = deque()
            queue.append((i, j))

            while queue:
                curr_i, curr_j = queue.popleft()
                if ((curr_i, curr_j)) not in visited:
                    visited.add((curr_i, curr_j))
                for dx, dy in directions:
                    next_i, next_j = curr_i + dx, curr_j + dy
                    if ( 0 <= next_i < rows and 0 <= next_j < cols and grid[next_i][next_j] == "1" and (next_i, next_j) not in visited):
                        queue.append((next_i, next_j))


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    traverse(i, j)
                    islands += 1
        return islands