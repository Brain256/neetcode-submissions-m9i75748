class Solution:
    def countSubstrings(self, s: str) -> int:
        seen = [[1] * len(s)]

        count = len(s)

        for i in range(1, len(s)): 
            results = []

            for j in range(len(s) - i): 
                if i == 1: 
                    if s[j] == s[j+i]: 
                        count += 1
                        results.append(1)
                    else: 
                        results.append(0)
                else: 
                    if s[j] == s[j+i] and seen[i-2][j+1]: 
                        count += 1
                        results.append(1)
                    else: 
                        results.append(0)
            
            seen.append(results)
        
        return count