class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for op in tokens: 
            if op.lstrip("-").isnumeric(): 
                stack.append(int(op))
            else: 
                first = stack.pop()
                second = stack.pop()
                res = 0

                if op == "+": 
                    res = first + second
                elif op == "-":
                    res = second - first
                elif op == "*":
                    res = first * second
                else: 
                    res = int(second / first)

                stack.append(res)

        
        return stack[0]

