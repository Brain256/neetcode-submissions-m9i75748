class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = []

        for s in stones: 
            minHeap.append(s * -1)

        heapq.heapify(minHeap) 

        while len(minHeap) > 1:
            first = minHeap[0] 

            heapq.heappop(minHeap)

            second = minHeap[0]

            heapq.heappop(minHeap)

            if first != second: 
                heapq.heappush(minHeap, first - second)
        

        if len(minHeap) > 0: 
            return minHeap[0] * -1
        else: 
            return 0

        
       
        