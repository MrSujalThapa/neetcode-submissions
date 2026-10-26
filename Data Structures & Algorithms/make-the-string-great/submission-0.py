class Solution:
    def makeGood(self, s: str) -> str:
        pass
        stack = []
        
        for letter in s:
            if len(stack) == 0:
                stack.append(letter)
            elif letter.lower() == stack[-1].lower():
                stack.pop()
            else:
                stack.append(letter)
        return "".join(stack)
            
