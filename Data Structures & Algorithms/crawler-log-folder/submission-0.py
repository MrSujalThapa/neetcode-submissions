class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for i in range(len(logs) - 1):
            if logs[i] == "./":
                pass
            elif logs[i] == "../":
                if len(logs) > 0:
                    stack.pop()
            else:
                stack.append(logs[i])
        
        return len(stack)
