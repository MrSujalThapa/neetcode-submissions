class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == "+":
                val = stack[0] + stack[1]
            elif tokens[i] == "-":
                 val = stack[0] - stack[1]
            elif tokens[i] == "*":
                 val = stack[0] * stack[1]
            elif tokens[i] == "/":
                 val = int(stack[0] / stack[1])
            else:
                stack.append(int(tokens[i]))
                continue
            stack.pop()
            stack.pop()
            stack.append(val)
        
        return stack[0]