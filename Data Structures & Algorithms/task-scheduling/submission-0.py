class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskHeap = []

        freqs = Counter(tasks)

        for f in freqs.values(): 
            heapq.heappush(taskHeap, -f)
        
        res = 0
       
        while True: 
            temp = []
            i = 0
            while i <= n and len(taskHeap): 
                res += 1
                i += 1
                front = -heapq.heappop(taskHeap)

                if front - 1 > 0: 
                    temp.append(-(front-1))

            for f in temp: 
                heapq.heappush(taskHeap, f)

            if not taskHeap:
                break
            else: 
                res += n - i + 1
                
                
            
        return res