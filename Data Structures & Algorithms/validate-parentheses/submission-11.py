class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for string in s:
            if string in ["[", "{", "("]:
                stack.append(string)
            elif len(stack) == 0:
                return False
            else: 
                if string == "}":
                    if stack[-1] == "{":
                        stack.pop()
                    else:
                        return False
                elif string == ")":
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
                elif string == "]":
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
        
        return not stack
