class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        my_dict = {}

        # my_list = []
        # sorted_data = sorted(heights, reverse=True)
        #
        result = []
        group_people = (item for item in zip(names, heights))
        
        sort_by_height =  sorted(group_people,key=lambda x:x[1], reverse=True)
        
        for name, height in sort_by_height:
            result.append(name)
            
        return " ".join(result)
        
       
              
s1 = Solution()
names = ["Mary","John","Emma"]
heights = [180,165,170]
print(s1.sortPeople(names,heights))