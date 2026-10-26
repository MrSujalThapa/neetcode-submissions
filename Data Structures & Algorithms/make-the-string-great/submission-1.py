class Solution:
    def makeGood(self, s: str) -> str:
        pass
        stack = []
        val = 0

        
        for letter in s:
            if letter.lower() != letter:
                val = abs(ord(letter) - ord("A"))
            else:
                val = abs(ord(letter.lower()) - ord("a"))
            if len(stack) == 0:
                stack.append(letter)
            elif ord(stack[-1]) - ord(letter) == 32:
                stack.pop()
            else:
                stack.append(letter)
        return "".join(stack)
            
