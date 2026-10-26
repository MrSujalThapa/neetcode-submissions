class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dups = {}
        final = []

        length = len(strs)

        for i in range(length):
            count = [0]*26
            for char in strs[i]:
                count[ord(char) - ord("a")] += 1
            
            key = tuple(count)
        
            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())

            
        
                
