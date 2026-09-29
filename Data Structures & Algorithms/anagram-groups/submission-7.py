class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramsMap = defaultdict(list)

        for s in strs: 
            freq = [0] * 26

            for c in s: 
                freq[ord(c) - ord('a')] += 1
            
            anagramsMap[tuple(freq)].append(s)
        
        return list(anagramsMap.values())

