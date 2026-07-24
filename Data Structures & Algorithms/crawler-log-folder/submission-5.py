class Solution:
    def minOperations(self, logs: List[str]) -> int:
        int = 0

        for i in range(len(logs)):
            if logs[i] == "./":
                pass
            elif logs[i] == "../":
                if int > 0:
                    int -= 1
            else:
                int += 1
        
        return int
