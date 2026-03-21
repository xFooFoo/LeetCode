'''
205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

Mapping 'e' to 'a'.
Mapping 'g' to 'd'.
Example 2:

Input: s = "f11", t = "b23"

Output: false

Explanation:

The strings s and t can not be made identical as '1' needs to be mapped to both '2' and '3'.

Example 3:

Input: s = "paper", t = "title"

Output: true

 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        my_dict = {}
        ascii_chars = [chr(i) for i in range(0, 128)]
        print(ascii_chars)
        for s, t in zip(s,t):
            if not my_dict.get(s):
                if t not in ascii_chars:
                    return False
                my_dict[s] = t
                ascii_chars.remove(t)
            else:
                if my_dict[s] != t:
                    return False
        return True
