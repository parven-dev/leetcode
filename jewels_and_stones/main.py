class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        my_jewel_dict = {}
        
        sum_of_jewels = 0
    
        for i in range(len(stones)):
            my_jewel_dict[stones[i]] = my_jewel_dict.get(stones[i], 0) + 1
         
        for j in range(len(jewels)):
            if jewels[j] in my_jewel_dict.keys():
                sum_of_jewels+=my_jewel_dict[jewels[j]]
            
        return sum_of_jewels

    
    
    


jewels = "aA"
stones = "aAAbbbb"

jewels = "ebd"
stones = "bbb"
s1 = Solution()
print(s1.numJewelsInStones(jewels, stones))