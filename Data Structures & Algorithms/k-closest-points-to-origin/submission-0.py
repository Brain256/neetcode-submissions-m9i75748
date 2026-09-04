class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pMap = {}
        minHeap = []
        res = []

        for p in points: 
            dist = math.sqrt(p[0] * p[0] + p[1] * p[1])

            heapq.heappush(minHeap, dist)

            if dist not in pMap: 
                pMap[dist] = [p]
            else: 
                pMap[dist].append(p)

        
        for i in range(k): 
            d = heapq.heappop(minHeap)

            res.append(pMap[d][-1])

            pMap[d].pop()

        return res