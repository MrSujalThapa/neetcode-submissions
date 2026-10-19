class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        right = 1
        count = 1
        index = 0

        if len(chars) == 1:
            return 1

        while right < len(chars):
            if chars[left] == chars[right]:
                count += 1
                right += 1
            else:
                chars[index] = chars[left]
                index += 1
                if count > 1:
                    for digit in str(count):
                        chars[index] = digit
                        index += 1
                count = 1
                left = right
                right += 1

        chars[index] = chars[left]
        index += 1
        if count > 1:
            for digit in str(count):
                chars[index] = digit
                index += 1
    
        return index
            