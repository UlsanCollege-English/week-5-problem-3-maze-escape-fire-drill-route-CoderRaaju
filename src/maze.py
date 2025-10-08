def find_path(grid, start, end):
    """
    Return a list of (r,c) from start to end inclusive, or None if no path.
    grid contains 0 (open) and 1 (wall). Moves: up/down/left/right only.
    """

    if not grid:
        return None

    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]

    sr, sc = start
    er, ec = end

    # Check start and end validity
    if not (0 <= sr < rows and 0 <= sc < cols and 0 <= er < rows and 0 <= ec < cols):
        return None
    if grid[sr][sc] == 1 or grid[er][ec] == 1:
        return None

    def dfs(r, c):
        # Out of bounds, wall, or already visited
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return None
        if grid[r][c] == 1 or visited[r][c]:
            return None

        # Mark current cell as visited
        visited[r][c] = True

        # Base case: reached end
        if (r, c) == end:
            return [(r, c)]

        # Explore 4 directions: up, down, left, right
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            path = dfs(r + dr, c + dc)
            if path:
                return [(r, c)] + path

        # Backtrack
        visited[r][c] = False
        return None

    return dfs(*start)
