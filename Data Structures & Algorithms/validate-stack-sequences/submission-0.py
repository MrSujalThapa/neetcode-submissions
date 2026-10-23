class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        left = 0
        stack = []
        right = 0

        for num in pushed:
            stack.append(num)
            if num == popped[right]:
                while stack and popped[right] == stack[-1]:
                    stack.pop()
                    right += 1
        
        return len(stack) == 0
                

            
            
            

