class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        
        while l < r: 
            if s[l] == s[r]: 
                l += 1
                r -= 1

            else: 
                s1 = s[l+1:r+1]
                s2 = s[l:r]
                if s1 == s1[::-1] or s2 == s2[::-1]:
                    return True
                
                return False
        
        return True