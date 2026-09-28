class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x: x[0])

        for interval in intervals: 
            if not res: 
                res.append(interval)
                continue
            
            if interval[0] <= res[-1][1]: 
                cur = res.pop()

                end = max(cur[1], interval[1])

                res.append([cur[0], end])
            
            else: 
                res.append(interval)

        return res
        
            

