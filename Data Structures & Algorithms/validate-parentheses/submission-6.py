class Solution:
    def isValid(self, s: str) -> bool:
        stack = []    
        #anytime we add a close character we need to check that the element before was same format then we can remove both elements
        #thus will only be true if stack is empty/remove works
        for i in range(len(s)):
            if s[i] in "[({":
                stack.append(s[i])
            elif len(stack) == 0:
                return False
            else:
                if s[i] == "]":
                    if stack[-1] != "[":
                        break
                elif s[i] == "}":
                    if stack[-1] != "{":
                        break
                else:
                    if stack[-1] != "(":
                        break
                        
                stack.pop()
        return len(stack) == 0 
            