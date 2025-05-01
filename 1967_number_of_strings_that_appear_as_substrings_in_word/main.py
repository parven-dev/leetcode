class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        counter = 0
        for string in patterns:
            if string in word or string == word:
                counter+=1

        return counter

patterns = ["a","abc","bc","d"]
word = "abc"

s1 = Solution()
print(s1.numOfStrings(patterns, word))