class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []

        for i in range(len(position)): 
            time = (target - position[i]) / speed[i]
            arr.append((position[i], time))

        stack = []

        arr.sort(reverse=True)

        for car in arr: 
            if not stack: 
                stack.append(car)
            
            else: 
                if car[1] > stack[-1][1]: 
                    stack.append(car)
            
        return len(stack)



        
        