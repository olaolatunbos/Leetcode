class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = {}
        heap = []
        res = []

        for point in points:
            distance = (point[0] ** 2) + (point[1] ** 2)
            distances[(point[0], point[1])] = distance
        
        for point in distances:
            heapq.heappush(heap, (distances[point], point))
        

        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        

        return res





        