class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = defaultdict(int)

        for num in nums: 
            numMap[num] += 1
        
        minHeap = []

        for key, count in numMap.items(): 
            heapq.heappush(minHeap, (count, key))

            if len(minHeap) > k: 
                heapq.heappop(minHeap)
            
        res = []

        for pair in minHeap: 
            res.append(pair[1])
        
        return res

