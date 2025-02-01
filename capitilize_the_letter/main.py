class Solution:
 
    def capitalizeTitle(self, title: str) -> str:
        title = title.split(" ")
        result = []
        for item in title:
            if len(item) <= 2:
                result.append(item.lower())
            else:
                result.append(item.capitalize())
            
        return " ".join(result)

                
            # elif len(item) <=2 and any(char.islower() for char in item):
            #     result.append(item.upper())
           
            
        # return " ".join(result)
            
    

# title = "capiTalIze tHe titLe"
title = "First leTTeR of EACH Word"

s1 = Solution()
print(s1.capitalizeTitle(title))