class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        left = 0
        right = 0

        while right < len(abbr):
            if abbr[right].isdigit():
                if abbr[right] == "0":
                    return False

                num = 0

                while right < len(abbr) and abbr[right].isdigit():
                    num = num * 10 + int(abbr[right])
                    right += 1

                left += num

            else:
                if left >= len(word) or word[left] != abbr[right]:
                    return False

                left += 1
                right += 1

        return left == len(word)