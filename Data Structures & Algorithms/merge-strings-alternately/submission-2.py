class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = []
        i = 0
        for s, t in zip(word1, word2):
            output.append(s)
            output.append(t)
            i += 1
        
        output.append(word1[i:])
        output.append(word2[i:])

        return "".join(output)