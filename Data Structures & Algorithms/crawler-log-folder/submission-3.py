class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for i in range(len(logs)):
            if logs[i] == "./":
                pass
            elif logs[i] == "../":
                if len(stack) != 0:
                    stack.pop()
            else:
                stack.append(logs[i])
        
        return len(stack)
