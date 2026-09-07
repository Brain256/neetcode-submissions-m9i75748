class Solution:
    def isHappy(self, n: int) -> bool:
        results = set()
        num = n

        while num != 1: 
            val = 0

            for c in str(num): 
                val += int(c) * int(c)
            
            if val in results: 
                return False
            
            results.add(val)
            num = val
    
        return True
