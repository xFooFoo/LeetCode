class Solution:
    def isPalindrome(self, x: int) -> bool:
        # We construct the number again as y
        x_copy = x
        y = 0
        while x_copy > 0:
           y *= 10
           y += x_copy % 10
           x_copy //= 10
        return x == y