class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
    
        for char in s: 
            if char in ['[', '(', '{']: 
                stack.append(char)
            else: 
                if not stack: return False

                c = stack.pop()

                if c == '[' and char != ']': 
                    return False
                if c == '{' and char != '}': 
                    return False
                if c == '(' and char != ')': 
                    return False
        
        return False if stack else True