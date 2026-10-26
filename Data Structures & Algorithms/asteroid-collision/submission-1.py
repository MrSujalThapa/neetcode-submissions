class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if stack and asteroid < 0 and stack[-1] > 0:
                if stack[-1] + asteroid < 0:
                    stack.pop()
                    stack.append(asteroid)
                elif stack[-1] + asteroid == 0:
                    stack.pop()
            else:
                stack.append(asteroid)
        
        return  stack
