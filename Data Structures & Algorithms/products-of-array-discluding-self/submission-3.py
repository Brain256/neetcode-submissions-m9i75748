class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        res = [1] * n

        value = 1
        for i in range(1, n): 
            value *= nums[i-1]
            res[i] *= value
            
        value = 1
        for i in range(n-2, -1, -1): 
            value *= nums[i+1]
            res[i] *= value
        
        return res


            
