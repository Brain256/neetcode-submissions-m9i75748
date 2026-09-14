class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []

        for i in range(len(position)): 
            t = (target - position[i]) / speed[i]
            arr.append((position[i], t))
        
        arr.sort(reverse = True)

        fleets = 0
        stack = []

        for car in arr: 
            if not stack: 
                stack.append(car)
            
            else: 
                front = stack[-1]

                if car[1] > front[1]: 
                    stack.append(car)
                else: 
                    continue

        
        return len(stack)



        
        