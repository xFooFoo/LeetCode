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

'''
Intuition - once the list of words is sorted in alphabetical order. The longest common prefix would be the maximum length of the shortest word which is now in index 0. We loop through the characters of this first word against the last word since this is the most different word and all characters in common between the two words would be considered the Longest Common Prefix since all the other words in between are "less different"
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        strs = sorted(strs) # This makes sure the shortest word is at the front & avoid OOB error
        firstWord = strs[0]
        lastWord = strs[-1]
        for i in range(len(firstWord)):
            if not firstWord[i] == lastWord[i]:
                return prefix
            prefix += firstWord[i]
        return prefix