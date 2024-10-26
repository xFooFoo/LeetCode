class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        largestStr = ""
        str1_len = len(str1)
        str2_len = len(str2)
        smallerStr = str2 if str1_len > str2_len else str1

        for i in range(0, len(smallerStr)):
            # check that the substring is a common denominator
            if (str1_len % (i+1) == 0 and str2_len % (i+1) == 0):
                # then check whether the substring "divides" both strings
                if (smallerStr[:i+1] * (str1_len // (i+1)) == str1 and smallerStr[:i+1] * (str2_len // (i+1)) == str2):
                    largestStr = smallerStr[:i+1]
        return largestStr