from collections import deque
def floodFill(image, sr, sc, color):
    visited = set() # (i, j)
    directions = [[0,1], [0,-1], [1, 0], [-1, 0]]
    rows, cols = len(image), len(image[0])
    original_color = image[sr][sc]

    def bfs(i, j):
        # queue
        queue = deque()
        # add first node to queue
        queue.append((i, j))
        while queue:
            # remove first element from queue
            curr_i, curr_j = queue.popleft()
            if (curr_i, curr_j) not in visited:
                visited.add((curr_i, curr_j))
            # add neighbours to queue
            for direction in directions:
                next_i, next_j = curr_i + direction[0], curr_j + direction[1]
                if 0 <= next_i < rows and 0 <= next_j < cols and image[next_i][next_j] == original_color:
                    queue.append((next_i, next_j))
    
    for i in range(rows):
        for j in range(cols):
            bfs(sr, sc)
    return visited


        
        
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2

print(floodFill(image, sr,sc, color))


