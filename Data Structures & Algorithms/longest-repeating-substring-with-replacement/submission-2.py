class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0

        charMap = defaultdict(int)
        maxFreq = 0
        maxLength = 0

        for r in range(len(s)):
            charMap[s[r]] += 1

            maxFreq = max(maxFreq, charMap[s[r]])

            while (r - l + 1) > maxFreq + k: 
                charMap[s[l]] -= 1
                l += 1

            maxLength = max(maxLength, r - l + 1) 

        return maxLength

