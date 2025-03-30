class Solution:
    def intersect(self, nums1:list[int], nums2: list[int]) -> list[int]:
        counter = {}
        for num in nums1:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        
        
        my_list = []
        for item in nums2:
            if item in counter and counter[item]>0:
                my_list.append(item)
                counter[item]-=1
        return my_list
            
            
            
            
s1 = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(s1.intersect(nums1, nums2))