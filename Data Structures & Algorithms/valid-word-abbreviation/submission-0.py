class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        left = 0
        right = 0
        isNum = False
        num = ""

        while left < len(word) and right < len(abbr):
            if abbr[right].isdigit():
                if num == "" and abbr[right] == "0":
                    return False

                num += abbr[right]
                right += 1
                isNum = True
                continue

            if isNum:
                left += int(num)
                num = ""
                isNum = False

                if left >= len(word):
                    return False

            if word[left] != abbr[right]:
                return False

            left += 1
            right += 1

        if isNum:
            left += int(num)

        return left == len(word) and right == len(abbr)