class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        string_index = 0
        sentence = sentence.split(" ")
        # print(sentence)
        for i in range(1, len(sentence)+1):
            # print(sentence[i-1])
            k = i - 1
            if sentence[k].startswith(searchWord):
                string_index=i
                break
        
        if string_index:
            return string_index
        else:
            return -1
    
    
    
sentence = "i love eating burger"
searchWord = "burg"
#output = 2

# sentence = "this problem is an easy problem"
# searchWord = "pro"
s1 = Solution()
print(s1.isPrefixOfWord(sentence, searchWord))