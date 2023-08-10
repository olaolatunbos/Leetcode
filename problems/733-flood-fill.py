class Solution:
    def floodFill(self, image, sr: int, sc: int, color: int):
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        rows, cols = len(image), len(image[0])
        visited = set()
        original_color = image[sr][sc]
        
        def bfs(i, j):
            queue = deque()
            queue.append((i, j))
            while queue:
                curr_i, curr_j = queue.popleft()
                if (curr_i, curr_j) not in visited:
                    visited.add((curr_i, curr_j))
                for direction in directions:
                    next_i, next_j = curr_i+direction[0], curr_j+direction[1]
                    if 0 <= next_i < rows and 0 <= next_j < cols and image[next_i][next_j] == original_color:
                        image[next_i][next_j] = color
                        queue.append((next_i, next_j))

                
        if image[sr][sc]== color:
            return image
        else:
            image[sr][sc]= color
            bfs(sr,sc)
        return image