class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""

        for st in strs: 
            s += str(len(st))
            s += ","
            s += st

        return s


    def decode(self, s: str) -> List[str]:


        if s == "":
            return []
        
        strs = []
        curLength = -1
        lenStr = ""
        st = ""

        for i in range(len(s)): 
            if curLength > 0: 
                st += s[i]
                curLength -= 1
            elif curLength <= 0 and s[i] == ",": 
                if curLength == 0: 
                    strs.append(st)
                    st = ""

                curLength = int(lenStr)
                lenStr = ""
            else:
                lenStr += s[i]

        strs.append(st)

        return strs




            



