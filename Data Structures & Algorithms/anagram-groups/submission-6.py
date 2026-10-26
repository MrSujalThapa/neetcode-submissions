class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = {}

        for word in strs:
            result = "".join(sorted(text))

            if result not in temp:
                temp[result] = []
            
            temp[result].append(word)


           # count = [0]*26

           # for char in word:
            #    count[ord(char) - ord("a")] += 1
            
            #key = tuple(count)

            #if key not in temp:
             #   temp[key] = []

           # temp[key].append(word)

        return list(temp.values())

            #idea behind this solution - loop through each word in array then loop through each character to create an array ie. aabb, [2,2,0...] then conver that array into a tuple because a dictionary needs to have unmutable keys. groups[key] } append the word to the responding key - meaning we're grouping anagrams together. from there we output only the values - return type is array but since values themselves are arrays they're split by array groups

