class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(" ")
        canBeTyped = len(words)
        for word in words:
            for letter in brokenLetters:
                if letter in word:
                    canBeTyped -= 1
                    break
        return canBeTyped