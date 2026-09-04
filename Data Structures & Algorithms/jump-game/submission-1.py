class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        cInd = 0

        while cInd < len(nums) - 1: 
            jumpLen = nums[cInd]

            if not jumpLen: 
                return False
            
            if cInd + jumpLen >= len(nums) - 1: 
                return True

            bestLen = 1

            for i in range(1, jumpLen+1): 
                
                if nums[cInd + i] + i > nums[cInd + bestLen] + bestLen: 
                    bestLen = i
            
            cInd += bestLen

        return True

            