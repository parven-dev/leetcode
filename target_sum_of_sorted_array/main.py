class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        sorted_nums = sorted(nums)
         
        
        
        my_list = []        
        for i in range(len(sorted_nums) ):
            if sorted_nums[i] == target:
                my_list.append(i)
      

        return my_list
    
        # for item in range(1, len(my_list)+1):
        #     print(item)
        #     my_list2.append(nums.index(nums[item]))
            
        
        # return my_list2

        # while left <= right:
        #     middle= (left + right) // 2 
            
        #     if target == nums[middle]:
        #         my_list.append(nums[middle])
        #         break
                
           
            
        #     elif target > nums[middle]:
        #         left = middle + 1
                
        #     else:
        #         right = middle - 1
            
                
            
            
            
            

# nums = [1,2,5,2,3]
# target = 2

nums = [1,2,5,2,3]
target = 3

s1 = Solution()
print(s1.targetIndices(nums, target))