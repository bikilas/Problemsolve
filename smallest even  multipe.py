class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 != 0:
            n *= 2  # If n is odd, double it to ensure the result is even
        return n
