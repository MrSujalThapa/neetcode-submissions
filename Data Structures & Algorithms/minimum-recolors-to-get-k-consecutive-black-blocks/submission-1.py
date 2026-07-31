class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white_count = 0

        # Count whites in the first window
#the idea behind this is that the window is size k, we start with the window size k and check the count of W ie ["W", "W"] min = 2. then we remove left from window and add right element if left element is white since it's leaving we reduce white count, if the right is white since it's entering window we increase the white count and we find the min everytime the window changes
        for i in range(k):
            if blocks[i] == "W":
                white_count += 1

        min_operations = white_count

        # Slide the window
        for right in range(k, len(blocks)):
            left = right - k

            # Remove the block leaving the window
            if blocks[left] == "W":
                white_count -= 1

            # Add the block entering the window
            if blocks[right] == "W":
                white_count += 1

            min_operations = min(min_operations, white_count)

        return min_operations