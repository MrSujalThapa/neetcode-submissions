class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == "+":
                val = stack[-1] + stack[-2]
            elif tokens[i] == "-":
                 val = stack[-2] - stack[-1]
            elif tokens[i] == "*":
                 val = stack[-2] * stack[-1]
            elif tokens[i] == "/":
                 val = int(stack[-2] / stack[-1])
            else:
                stack.append(int(tokens[i]))
                continue
            stack.pop()
            stack.pop()
            stack.append(val)
        
        return stack[-1]