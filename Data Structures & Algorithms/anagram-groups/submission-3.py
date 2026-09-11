class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs: 
            arr = [0] * 26

            for c in s: 
                arr[ord(c) - ord("a")] += 1
            
            key = tuple(arr)

            d[key].append(s)
        
        res = []
        for arr in d.values(): 
            res.append(arr)

        return res