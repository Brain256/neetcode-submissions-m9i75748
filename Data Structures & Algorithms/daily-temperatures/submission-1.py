class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, v in enumerate(temperatures):  
            while stack and v > stack[-1][0]: 
                value = stack.pop()
                res[value[1]] = i - value[1]
            
            stack.append((v, i))
        
        return res 
            
           

