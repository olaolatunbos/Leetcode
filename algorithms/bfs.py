from collections import deque
def breadthFirstSearch(matrix):
    visited = set() #(i, j)
    directions = [[0,1], [0,-1], [1, 0], [-1, 0]]
    rows, cols = len(mat), len(mat[0])

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
                if 0 <= next_i < rows and 0 <= next_j < cols:
                    queue.append((next_i, next_j))
    
    for i in range(rows):
        for j in range(cols):
            bfs(i, j)
    return visited





        
        
mat = [[1,1], [1,0]]

print(breadthFirstSearch(mat))


