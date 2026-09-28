class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for point in points: 
            distance = math.sqrt(point[0] ** 2 + point[1] ** 2)
            heapq.heappush(minHeap, (distance, point[0], point[1]))
        
        res = []

        while len(res) < k: 
            value = heapq.heappop(minHeap)
        
            res.append([value[1], value[2]])
        
        return res