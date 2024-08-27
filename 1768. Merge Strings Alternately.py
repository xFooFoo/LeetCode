class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_word = ""
        word1_list = list(word1)
        word2_list = list(word2)
        while (word1_list and word2_list):
            merged_word += word1_list.pop(0)
            merged_word += word2_list.pop(0)
        while (word1_list):
            merged_word += word1_list.pop(0)
        while (word2_list):
            merged_word += word2_list.pop(0)
        return merged_word 
        