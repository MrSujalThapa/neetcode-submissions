class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            alive = True

            # Collision only when stack top moves right
            # and current asteroid moves left
            while alive and stack and stack[-1] > 0 and asteroid < 0:
                if stack[-1] < abs(asteroid):
                    stack.pop()  # current asteroid keeps moving left
                elif stack[-1] == abs(asteroid):
                    stack.pop()
                    alive = False  # both explode
                else:
                    alive = False  # current asteroid explodes

            if alive:
                stack.append(asteroid)

        return stack