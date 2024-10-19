'''
392. Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # read every letter and index of t into a dict
        t_dict = {}
        for i in range(0, len(t)):
            t_dict.setdefault(t[i], []).append(i)

        # check every letter in s can be made relatively
        currentIndex = -1
        
        for char in s:
            print(char)
            updatedIndex = False
            if char in t_dict:
                for idx in t_dict[char]:
                    if idx > currentIndex:
                        print(f"Char: {char}, idx: {idx}, currentIndex: {currentIndex}")
                        currentIndex = idx
                        updatedIndex = True
                        break
            else:
                return False

            if not updatedIndex:
                return False
            
        return True


# s = "acb"
# t = "ahbgdc"
# print(Solution().isSubsequence(s, t))