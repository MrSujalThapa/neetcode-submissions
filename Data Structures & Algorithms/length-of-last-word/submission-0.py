class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        firstLetter = False;
        i = len(s) - 1
        length = 0
       
        while i >= 0:
            if (not firstLetter and s[i] == " "): 
                i -=1
                continue
            firstLetter = True
            if (s[i] == " "):
                break
            length +=1
            i -=1
        return length