class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        st = ""

        for i in range(1, len(path)): 
            if path[i] == "/": 
                if st == "..": 
                    if len(res):
                        res.pop()
                    
                    st = ""

                    continue
                
                if st and st != ".":
                    res.append(st)
                
                st = ""
            
            else: 
                st += path[i]
        
        if st != "." and st != ".." and st:
            res.append(st)
        
        if st == ".." and len(res):
            res.pop()
            
        return "/" + "/".join(res)