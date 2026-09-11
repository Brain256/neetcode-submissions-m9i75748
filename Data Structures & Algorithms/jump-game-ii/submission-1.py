class Solution:
    def jump(self, nums: List[int]) -> int:
        
        curIndex = 0
        numJumps = 0

        while curIndex < len(nums)-1: 

            curJumps = nums[curIndex]

            if curIndex + curJumps >= len(nums)-1: 
                numJumps += 1
                break

            bestJump = 0
            bestDist = 0

            for i in range(1, curJumps+1): 
                
                if i + nums[curIndex + i] > bestDist: 
                    bestDist = i + nums[curIndex + i]
                    bestJump = i
            
            curIndex += bestJump
            numJumps += 1
        
        return numJumps