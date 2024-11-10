'''
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        strs = sorted(strs) # This makes sure the shortest word is at the front & avoid OOB error
        numberOfWords = len(strs)
        firstWord = strs[0]
        for i in range(len(firstWord)):
            for j in range(1,numberOfWords):
                if not firstWord[i] == strs[j][i]:
                    return prefix
            prefix += firstWord[i]
        return prefix