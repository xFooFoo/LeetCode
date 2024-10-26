'''
345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
'''


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "AaEeIiOoUu"
        # Python Strings are immutable so we use lists
        s_list = list(s)
        i = 0 # LHS index
        j = len(s_list) - 1 #RHS index
        while i < j:
            while i < j and s_list[i] not in vowels:
                i += 1
            while i < j and s_list[j] not in vowels:
                j -= 1
            # Vowels found -> Swap
            # print(f"Performing swap on i{i} j{j}")
            if i < j:
                s_list[i], s_list[j] = s_list[j], s_list[i]
            # update index
            i += 1
            j -= 1
        return "".join(s_list)

print(Solution().reverseVowels("leetcode"))