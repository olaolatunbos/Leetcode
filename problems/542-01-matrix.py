class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        queue = []

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] == "*"
        
        for i, j in queue:
            for dr, dc in directions:
                next_i, next_j = i + dr, j + dc
                if 0 <= next_i < rows and 0<= next_j < cols and mat[next_i][next_j] == "*":
                    mat[next_i][next_j] = mat[i][j] + 1
                    queue.append((next_i, next_j))
        
        return mat

        
        


