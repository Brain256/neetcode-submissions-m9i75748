class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        right = 0
        maxLength = 0

        freqSet = set()

        while right < len(s): 
            while s[right] in freqSet:
                freqSet.remove(s[left])
                left += 1
            
            freqSet.add(s[right])
            right += 1
            maxLength = max(right - left, maxLength)
        
        return maxLength

        