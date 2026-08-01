class Solution:
    def maxSatisfied(
        self,
        customers: List[int],
        grumpy: List[int],
        minutes: int
    ) -> int:
        satisfied = 0
        extra = 0

        for i in range(len(customers)):
            if grumpy[i] == 0:
                satisfied += customers[i]

        for i in range(minutes):
            if grumpy[i] == 1:
                extra += customers[i]

        max_extra = extra
        left = 0

        for right in range(minutes, len(customers)):
            if grumpy[right] == 1:
                extra += customers[right]

            if grumpy[left] == 1:
                extra -= customers[left]

            left += 1
            max_extra = max(max_extra, extra)

        return satisfied + max_extra