'''
1268. Search Suggestions System

You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.

 

Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
After typing mou, mous and mouse the system suggests ["mouse","mousepad"].
Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Explanation: The only word "havana" will be always suggested while typing the search word.
 

Constraints:

1 <= products.length <= 1000
1 <= products[i].length <= 3000
1 <= sum(products[i].length) <= 2 * 104
All the strings of products are unique.
products[i] consists of lowercase English letters.
1 <= searchWord.length <= 1000
searchWord consists of lowercase English letters.
'''
class Solution:
    def __init__(self):
        self.root = {}
        self.results = []

    def addProducts(self, products: List[str]):
        for product in products:
            curr = self.root
            for letter in product:
                if letter not in curr:
                    curr[letter] = {}
                curr = curr[letter]
            curr['*'] = {} # Denotes the end of a word
    
    def dfs(self, curr: Dict[str, Dict[str, str]], result: List[str], word: str) -> List[str]:
        if len(result) == 3:
            return
        if '*' in curr:
            result.append(word)
        
        for key in sorted(curr.keys()):
            self.dfs(curr[key], result, word + key)
        return result

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        self.addProducts(products)
        curr = self.root
        for idx, letter in enumerate(searchWord):
            if letter in curr:
                curr = curr[letter]
                self.results.append(self.dfs(curr, [], searchWord[:idx+1]))
            else:
                self.results.append([])
                break
        self.results.extend([[] for _ in range(len(self.results), len(searchWord))])
        return self.results