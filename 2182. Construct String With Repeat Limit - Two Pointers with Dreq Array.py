'''
2182. Construct String With Repeat Limit

You are given a string s and an integer repeatLimit. Construct a new string repeatLimitedString using the characters of s such that no letter appears more than repeatLimit times in a row. You do not have to use all characters from s.

Return the lexicographically largest repeatLimitedString possible.

A string a is lexicographically larger than a string b if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b. If the first min(a.length, b.length) characters do not differ, then the longer string is the lexicographically larger one.

 

Example 1:

Input: s = "cczazcc", repeatLimit = 3
Output: "zzcccac"
Explanation: We use all of the characters from s to construct the repeatLimitedString "zzcccac".
The letter 'a' appears at most 1 time in a row.
The letter 'c' appears at most 3 times in a row.
The letter 'z' appears at most 2 times in a row.
Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
The string is the lexicographically largest repeatLimitedString possible so we return "zzcccac".
Note that the string "zzcccca" is lexicographically larger but the letter 'c' appears more than 3 times in a row, so it is not a valid repeatLimitedString.
Example 2:

Input: s = "aababab", repeatLimit = 2
Output: "bbabaa"
Explanation: We use only some of the characters from s to construct the repeatLimitedString "bbabaa". 
The letter 'a' appears at most 2 times in a row.
The letter 'b' appears at most 2 times in a row.
Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
The string is the lexicographically largest repeatLimitedString possible so we return "bbabaa".
Note that the string "bbabaaa" is lexicographically larger but the letter 'a' appears more than 2 times in a row, so it is not a valid repeatLimitedString.
 

Constraints:

1 <= repeatLimit <= s.length <= 105
s consists of lowercase English letters.
'''

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        sorted_s = ''.join(sorted(s))
        base_ord = ord('z') # largest char will have index 0 -> 25
        # Build a freq map and each time gathering the max such that the repeatLimit isn't met
        freq = [0] * 26
        largestIdx = 0 # Index of the largest lexicographically letter
        nextIdx = 0
        res = ""

        for c in sorted_s:
            idx = ord('z') - ord(c)
            freq[idx] += 1

        while nextIdx < 26 and largestIdx < 26:
            while largestIdx < 26 and freq[largestIdx] == 0:
                largestIdx += 1
            if not largestIdx < 26:
                break

            largestChr = chr(ord('z') - largestIdx)
            if freq[largestIdx] <= repeatLimit:
                res += largestChr * freq[largestIdx]
                freq[largestIdx] -= freq[largestIdx]
                largestIdx += 1
            else:
                res += largestChr * repeatLimit
                freq[largestIdx] -= repeatLimit
                nextIdx = largestIdx + 1

                while nextIdx < 26 and freq[nextIdx] == 0:
                    nextIdx += 1
                if nextIdx < 26:
                    nextChr = chr(ord('z') - nextIdx)
                    res += nextChr
                    freq[nextIdx] -= 1
                else:
                    break
        return res
