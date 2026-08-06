class Solution:
    def rob(self, nums: List[int]) -> int:
        def recurse(i, end, memo): 
            if i >= end: 
                return 0

            if i in memo: 
                return memo[i]

            memo[i] = max(recurse(i+2, end, memo) + nums[i], recurse(i+1, end, memo))

            return memo[i]

        l = len(nums)
        if l == 1: 
            return nums[0]

        return max(recurse(0, l-1, {}), recurse(1, l, {}))