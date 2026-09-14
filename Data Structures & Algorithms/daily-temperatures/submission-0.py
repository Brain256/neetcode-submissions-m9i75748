class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tempStack = []
        res = [0] * len(temperatures)

        for i, v in enumerate(temperatures): 
            if not tempStack: 
                tempStack.append((v, i)) 
            
            else: 
                while tempStack and v > tempStack[-1][0]: 
                    res[tempStack[-1][1]] = i - tempStack[-1][1]
                    tempStack.pop()
                
                tempStack.append((v, i))
        
        return res

