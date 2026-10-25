class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        combined = sorted(zip(position, speed), reverse=True)
        sorted_position, sorted_speed = zip(*combined)

        for i, position in enumerate(sorted_position):
            time = (target - position)/sorted_speed[i]
            if stack and time <= stack[-1]:
                continue
            else:
                stack.append(time)

        return len(stack)

        
        

        