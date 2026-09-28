class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = defaultdict(int)

        for num in nums: 
            freqMap[num] += 1
        
        freqList = [[] for _ in range(len(nums)+1)]

        for key, count in freqMap.items(): 
            freqList[count].append(key)

        res = []

        for i in range(len(nums), -1, -1): 
            if not freqList[i]: 
                continue

            for freq in freqList[i]: 
                if len(res) == k: 
                    return res

                res.append(freq)
    
        return res