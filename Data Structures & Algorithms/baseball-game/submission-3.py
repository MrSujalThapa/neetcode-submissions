class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        index = 0

        for operation in operations:
            if operation == "C":
                index -= 1
                stack.pop()
            elif operation == "D":
                stack.append(int(stack[index-1])*2)
                index += 1
            elif operation == "+":
                stack.append(int(stack[index-1]) + int(stack[index-2]))
                index += 1
            else:
                stack.append(int(operation))
                index += 1
        
        sum = 0
        for num in stack:
            sum += num
        return sum
