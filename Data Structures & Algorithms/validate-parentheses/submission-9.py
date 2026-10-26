class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) == 1:
            return False

        for string in s:
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
            else:
                stack.append(string)
        
        if len(stack) == 0:
            return True
        else:
            return False
