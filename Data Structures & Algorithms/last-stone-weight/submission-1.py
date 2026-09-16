class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []

        for stone in stones: 
            heapq.heappush(maxHeap, -stone)

        while len(maxHeap) > 1: 
            first = -heapq.heappop(maxHeap)
            second = -heapq.heappop(maxHeap)

            if first > second: 
                heapq.heappush(maxHeap, -(first - second))
            
        if maxHeap: 
            return -maxHeap[0]
        else: 
            return 0