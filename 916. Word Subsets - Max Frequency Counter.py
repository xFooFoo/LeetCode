'''
916. Word Subsets

You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.

 

Example 1:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]
Example 2:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
Output: ["apple","google","leetcode"]
 

Constraints:

1 <= words1.length, words2.length <= 104
1 <= words1[i].length, words2[i].length <= 10
words1[i] and words2[i] consist only of lowercase English letters.
All the strings of words1 are unique.
'''
from collections import Counter
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # we want words in words1 that all words in words2 are a subset of
        # Intuition, Build a max freq map/dict from words2 and iterate through words1 and build a freq map for 
        # each word to find whether there are any differences

        universal_words = []
        # Create an empty Counter to store maximum counts
        max_counter = Counter()

        words2_counter = [Counter(word) for word in words2]
        for counter in words2_counter:
            for key, count in counter.items():
                max_counter[key] = max(max_counter[key], count) # Store only the highest count for each char
        
        for word in words1:
            word1_counter = Counter(word)
            # print(word1_counter)
            # print("Difference:", max_counter - word1_counter)
            #if sum((max_counter - word1_counter).values()) == 0:
            if len(max_counter - word1_counter) == 0:
                universal_words.append(word)
        
        return universal_words