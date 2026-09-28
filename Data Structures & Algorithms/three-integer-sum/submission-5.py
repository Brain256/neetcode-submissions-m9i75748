class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)): 

            if i > 0 and nums[i] == nums[i-1]: 
                continue

            target = -nums[i]
            l, r = i+1, len(nums)-1

            while l < r: 
                
                while l > i+1 and nums[l] == nums[l-1]: 
                    l += 1
                
                if l == r: 
                    break

                value = nums[l] + nums[r]

                if value == target: 
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif value < target: 
                    l += 1
                else: 
                    r -= 1

        return res

