class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        arr1 = [-1] * len(cost)
        arr2 = [-1] * len(cost)

        def dfs(i, arr): 
            if i >= len(cost) - 2: 
                return cost[i]
            
            if arr[i] != -1: 
                return arr[i]

            arr[i] = min(cost[i] + dfs(i+1, arr), cost[i] + dfs(i+2, arr))

            return arr[i]
        
        return min(dfs(0, arr1), dfs(1, arr2))