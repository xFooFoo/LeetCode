'''
67. Add Binary

Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        output = ""
        carry = 0
        len_a = len(a)
        len_b = len(b)
        diff = abs(len_a-len_b)

        if len_a > len_b:
            b = "0" * diff + b
            len_b += diff
        else:
            a = "0" * diff + a
            len_a += diff

        for i in range(len_a-1, -1, -1):
            #print(f'int(a) {int(a)} int(b) {int(b)}')
            bitSum = int(a[i]) + int(b[i]) + carry
            if bitSum == 0:
                output = "0" + output
            elif bitSum == 1:
                if carry:
                    carry -= 1 
                output = "1" + output
            elif bitSum == 2:
                if carry:
                    carry -= 1 
                output = "0" + output
                carry += 1
            elif bitSum == 3:
                # keep the carry i.e. don't decrement
                output = "1" + output

        if carry:
            output = "1" + output
        return output