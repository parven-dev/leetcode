class Solution:
    def splitWordsBySeparator(self, words: list[str], separator: str) -> list[str]:
        my_list = []
        # print(words[1].split("."))
        for item in  words:
            my_list.extend([i for i in item.split(separator) if i])
        return my_list
            
            
            
            # if separator in words[i]:
            #     data = words[i].split(separator)
            #     print(data)
            #     get+=str(data)
            #     data1 = " ".join(data)
            #     my_list.append(data1)
            #     # my_list.append(data)
                
            # elif separator not in words[i]:
            #     # my_list.append("".join(words[i]))
            #     my_list.append(words[i])
           
            # elif separator not in words[i]:
            #     my_list.append(words[i])
           
            
        
            
            

words = ["one.two.three","four.five","six"]
separator = "."

s1 = Solution()
print(s1.splitWordsBySeparator(words, separator))