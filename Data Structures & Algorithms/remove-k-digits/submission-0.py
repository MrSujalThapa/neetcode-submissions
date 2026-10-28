
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        right = 0

        while right < len(num):
            val = num[right]

            while stack and k > 0 and val < stack[-1]:
                stack.pop()
                k -= 1

            stack.append(val)
            right += 1

        while k > 0:
            stack.pop()
            k -= 1

        result = "".join(stack).lstrip("0")
        return result if result else "0"
