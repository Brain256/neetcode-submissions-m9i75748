class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1Freq = [0] * 26
        s2Freq = [0] * 26

        for i in range(len(s1)): 
            s1Freq[ord(s1[i]) - ord('a')] += 1

            if i < len(s2): 
                s2Freq[ord(s2[i]) - ord('a')] += 1

        for i in range(len(s1), len(s2)):  
            
            if s1Freq == s2Freq: 
                return True
            
            s2Freq[ord(s2[i]) - ord('a')] += 1
            s2Freq[ord(s2[i - len(s1)]) - ord('a')] -= 1

        return s1Freq == s2Freq  
