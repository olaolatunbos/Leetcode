from collections import deque
def breadthFirstSearch(matrix):
    visited = [] #(i, j)
    directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
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
                visited.append((curr_i, curr_j))
            # add neighbours to queue
            for direction in directions:
                next_i, next_j = curr_i + direction[0], curr_j + direction[1]
                if 0 <= next_i < rows and 0 <= next_j < cols and (next_i, next_j) not in visited:
                    queue.append((next_i, next_j))

    
    for i in range(rows):
        for j in range(cols):
            bfs(i, j)
    return visited





# visits children on (0,0) first as it is first in for loop     
mat = [[1,1], [1,0]]

print(breadthFirstSearch(mat))

# def bfs(matrix):
#   # Check for an empty matrix/graph.
#   if not matrix:
#     return []

#   rows, cols = len(matrix), len(matrix[0])
#   visited = set()
#   directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

#   def traverse(i, j):
#     queue = deque([(i, j)])
#     while queue:
#       curr_i, curr_j = queue.popleft()
#       if (curr_i, curr_j) not in visited:
#         visited.add((curr_i, curr_j))
#         # Traverse neighbors.
#         for direction in directions:
#           next_i, next_j = curr_i + direction[0], curr_j + direction[1]
#           if 0 <= next_i < rows and 0 <= next_j < cols:
#             # Add in question-specific checks, where relevant.
#             queue.append((next_i, next_j))

#   for i in range(rows):
#     for j in range(cols):
#       traverse(i, j)


