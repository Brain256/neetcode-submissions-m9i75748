class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs: 
            arr = [0] * 26

            for c in s: 
                arr[ord(c) - ord("a")] += 1
            
            key = "-".join(map(str, arr))

            d[key].append(s)

        return list(d.values())