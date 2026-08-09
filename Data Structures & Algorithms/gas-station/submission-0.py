class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        startInd = -1
        total = 0 
        curTotal = 0

        for i in range(len(cost)): 
            net = gas[i] - cost[i]

            total += net
            curTotal += net

            if startInd == -1 and net >= 0:
                startInd = i 
                curTotal = net

            if curTotal < 0: 
                startInd = -1
                curTotal = 0
        
        if total < 0: 
            return -1
        else: 
            return startInd