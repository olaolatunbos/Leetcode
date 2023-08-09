from collections import deque

def bfs(matrix, sr, sc):
  # Check for an empty matrix/graph.
  if not matrix:
    return []

  rows, cols = len(matrix), len(matrix[0])
  visited = set()
  directions = ((0, 1), (0, -1), (1, 0), (-1, 0)) # right, left, up, down

  def traverse(i, j):
    queue = deque([(i, j)])
    while queue:
      curr_i, curr_j = queue.popleft() # pop first element in queue
      if (curr_i, curr_j) not in visited:
        visited.add((curr_i, curr_j)) # if not in visited add to visited
        # Traverse neighbours.
        for direction in directions:
          next_i, next_j = curr_i + direction[0], curr_j + direction[1]
          if 0 <= next_i < rows and 0 <= next_j < cols and matrix[next_i][next_j] == 1:
            # Add neighbours
            queue.append((next_i, next_j))

    if image[sr][sc] == 1:
      traverse(sr,sc)
    else:
      return - 1
    return visited

image = [[1,1,1],[1,1,0],[1,0,1]]

print(bfs(image,0,0))



queue = deque()
queue.append(1)
print(queue)