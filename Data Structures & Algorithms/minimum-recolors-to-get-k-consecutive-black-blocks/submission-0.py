class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white_count = 0

        # Count whites in the first window
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