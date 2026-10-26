class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        val = 0

        for token in tokens:
            if token == "+":
                val = stack[-1] + stack[-2]
                stack.pop()
                stack.pop()
                stack.append(int(val))
            elif token == "*":
                val = stack[-1]*stack[-2]
                stack.append(int(val))
            elif token == "-":
                val = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(int(val))
            else:
                stack.append(int(token))
        return stack[-1]

