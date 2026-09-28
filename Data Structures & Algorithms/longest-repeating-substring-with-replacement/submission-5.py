class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left, right = 0, 0
        freqMap = defaultdict(int)
        maxLength = 0

        maxFreq = 0

        while right < len(s):
            freqMap[s[right]] += 1  

            maxFreq = max(maxFreq, freqMap[s[right]])

            while right - left + 1 - maxFreq > k: 
                freqMap[s[left]] -= 1
            
                left += 1

            right += 1
            maxLength = max(right - left, maxLength)
            

        return maxLength
            



