'''
58. Length of Last Word

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
'''

'''
Intuition
We want to obtain the last word and return the length of it. This can be done by splitting the string with the " " space delimiter.

Approach
We then split the string s by the default space delimiter** and this gives us a list of all the words without the spaces.
We access the last word by using negative indexing on the list i.e. [-1]
Viola! We can now use the len() function to return the length of the last word!
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])