class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current = ""
        count = 0

        for char in s:
            if char.isdigit():
                count = count * 10 + int(char)

            elif char == "[":
                stack.append((current, count))
                current = ""
                count = 0

            elif char == "]":
                prev, repeat = stack.pop()
                current = prev + current * repeat

            else:
                current += char

        return current