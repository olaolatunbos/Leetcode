def dfs(matrix):
  # Check for an empty matrix/graph.
  if not matrix:
    return []

  rows, cols = len(matrix), len(matrix[0])
  visited = []
  directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

  def traverse(i, j):
    # base case
    if (i, j) in visited:
      # A return statement is used to end the execution of the function call, returns None
      return

    visited.append((i, j))
    # Traverse neighbors.
    for direction in directions:
      next_i, next_j = i + direction[0], j + direction[1]
      if 0 <= next_i < rows and 0 <= next_j < cols:
        # Add in question-specific checks, where relevant.
        # recursive call
        traverse(next_i, next_j)

  for i in range(rows):
    for j in range(cols):
      traverse(i, j)
  return visited

mat = [[1,1], [1,1]]
print(dfs(mat))