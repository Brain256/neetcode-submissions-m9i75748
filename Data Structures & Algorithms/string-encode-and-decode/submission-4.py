class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        j = 0

        while i < len(s):
            while s[j] != "#":
                j += 1

            strLength = int(s[i:j])
            i = j + 1
            j = i + strLength
            res.append(s[i:j])
            i = j

        return res