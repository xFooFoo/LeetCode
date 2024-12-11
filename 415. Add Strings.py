'''
415. Add Strings

Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"
 

Constraints:

1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.
'''
from itertools import zip_longest
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        numbers_dict = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9
        }

        totalSum = ""
        carry = 0

        for n1, n2 in zip_longest(reversed(num1), reversed(num2), fillvalue="0"):
            currSum = numbers_dict[n1] + numbers_dict[n2] + carry
            if currSum >= 10:
                currSum -= 10
                carry = 1
            else:
                carry = 0

            totalSum = str(currSum) + totalSum
        
        if carry:
            totalSum = "1" + totalSum
        
        return totalSum

