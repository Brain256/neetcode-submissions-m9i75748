class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        maxHeap = []
        res = []

        for key, val in count.items():
            heapq.heappush(maxHeap, (-val, key))

        for i in range(k): 
            res.append(heapq.heappop(maxHeap)[1])

        return res

