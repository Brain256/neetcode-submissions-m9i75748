class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for num in nums: 
            newPerms = []
            for p in perms: 
                for i in range(len(p)+1): 
                    newPerm = p.copy()
                    newPerm.insert(i, num)
                    newPerms.append(newPerm)
                
            perms = newPerms
        
        return perms


