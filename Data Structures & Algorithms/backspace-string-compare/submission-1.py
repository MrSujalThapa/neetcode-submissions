class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        left = len(s) - 1
        right = len(t) - 1

        while left >= 0 or right >= 0:
            skipS = 0
            skipT = 0

            while left >= 0:
                if s[left] == "#":
                    skipS += 1
                    left -= 1
                elif skipS > 0:
                    skipS -= 1
                    left -= 1
                else:
                    break

            while right >= 0:
                if t[right] == "#":
                    skipT += 1
                    right -= 1
                elif skipT > 0:
                    skipT -= 1
                    right -= 1
                else:
                    break

            if left >= 0 and right >= 0:
                if s[left] != t[right]:
                    return False
            elif left >= 0 or right >= 0:
                return False

            left -= 1
            right -= 1

        return True