class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        maxLen = 0

        for num in nums: 
            if num - 1 in numSet: 
                continue
            
            curLen = 1
            temp = num

            while temp+1 in numSet: 
                curLen += 1
                temp += 1
                
            maxLen = max(curLen, maxLen)
        
        return maxLen