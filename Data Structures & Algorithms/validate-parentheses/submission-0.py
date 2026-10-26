class Solution:
    def isValid(self, s: str) -> bool:
        stack = []    
        #anytime we add a close character we need to check that the element before was same format then we can remove both elements
        #thus will only be true if stack is empty/remove works

        for i in range(len(s)):
            if s[i] == "]":
                if stack[-1] != "[":
                    break
                else:
                    stack.pop()
            elif s[i] == "}":
                if stack[-1] != "{":
                    break
                else:
                    stack.pop()
            elif s[i] == ")":
                if stack[-1] != "(":
                    break
                else:
                    stack.pop()
            else:
                stack.append(s[i])

        return len(stack) == 0 
            