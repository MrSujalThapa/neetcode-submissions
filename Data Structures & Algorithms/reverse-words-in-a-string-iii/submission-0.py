class Solution:
    def reverseWords(self, s: str) -> str:
        pass
        def reverse(word):
            ordWord = []
            j = len(word) - 1
            while j >= 0:
                ordWord.append(word[j])
                j -= 1   
            return "".join(ordWord)

        output = []

        left = 0
        right = 0

        while right < len(s):
            if right + 1 < len(s):
                if s[right + 1] == " ":
                    output.append(reverse(s[left:right + 1]))
                    right += 2
                    left = right
                else:
                    right += 1
            else:
                output.append(reverse(s[left:]))
                break
        
        return " ".join(output)




        