class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []

        for num in nums: 
            heapq.heappush(maxHeap, -num)
        
        popped = 0

        while popped < k-1: 
            heapq.heappop(maxHeap)
            popped += 1
        
        return -heapq.heappop(maxHeap)