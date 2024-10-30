'''
394. Decode String

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
 

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
'''

'''
Approach:
Keep adding characters to the stack until you encounter a "]" 
where we would start popping from the stack to construct an encoded_string that will be multiplied by "k" 
and appended back into the stack since it can be multiplied again if more "]" are encountered.
Once we have processed the whole string "s", we can join whatever's in the stack and return it.
'''

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        encoded_string = ""
        k = ""
        for chr in s:
            if chr.isdigit():
                k += chr
            elif chr == "[":
                stack.append(k)
                k = ""
            elif chr != "]":
                stack.append(chr)
            else:
                while not stack[-1].isdigit():
                    encoded_string = stack.pop() + encoded_string
                else:
                    encoded_string = int(stack.pop()) * encoded_string
                    stack.append(encoded_string)
                    encoded_string = ""
        return "".join(stack)