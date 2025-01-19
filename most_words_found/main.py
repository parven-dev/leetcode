class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        
        # sentences =  sentences.split(",")
        # sentences = ",".join(sentences)
        # sentences =  (sentences.split(","))
        # return len(sentences[0])
        data = []
        
        for i in range(len(sentences)):
            data.append(sentences[i].split(" "))


        result = []
        for item in data:
            result.append(len(item))
            
        return max(result)
        # print(data)
        # max_len = max(data)
        # print(max_len)
        # return len(max_len)
    
            
    
    
s1 = Solution()
# sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
sentences = ["please wait", "continue to fight", "continue to win"]
print(s1.mostWordsFound(sentences))