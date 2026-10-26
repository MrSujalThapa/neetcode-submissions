class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []



        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] <= temp:
                j = stack.pop()
                temperatures[j] = i - j

            stack.append(i)

        for val in stack:
            temperatures[val] = 0

        return temperatures