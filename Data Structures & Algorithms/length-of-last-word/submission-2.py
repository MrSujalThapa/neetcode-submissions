class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #Input: s = "   fly me   to   the moon  "
        count = 0
        space = True

        for i in range(len(s) -1,-1,-1 ):
            if s[i] == " " and space:
                continue
            if s[i] == " ":
                return count
            space = False
            count += 1