class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        taskHeap = []

        for key, item in freq.items(): 
            heapq.heappush(taskHeap, -item)

        taskQueue = deque()
        curTime = 0

        while taskQueue or taskHeap: 

            while taskQueue and curTime >= taskQueue[0][0]: 
                front = taskQueue.popleft()
                heapq.heappush(taskHeap, front[1])

            if taskHeap: 
                front = heapq.heappop(taskHeap)
                
                if front + 1 != 0: 
                    taskQueue.append((curTime + n + 1, front + 1))
            
            curTime += 1
 
        return curTime










