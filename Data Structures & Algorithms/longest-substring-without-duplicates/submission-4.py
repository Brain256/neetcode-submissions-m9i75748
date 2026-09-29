class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0

        maxLength = 0
        freq = set()

        for r in range(len(s)): 
            if s[r] not in freq:
                maxLength = max(maxLength, r - l + 1)
                freq.add(s[r])

            else: 
                while s[r] in freq: 
                    freq.remove(s[l])
                    l += 1
                
                freq.add(s[r])
            
        return maxLength

        


        