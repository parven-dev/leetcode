class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        
        result = []
        
        for image_list in image:
            new_image = []
            for images in image_list[::-1]:
                
                if images == 0:
                    new_image.append(1)
                else:
                    new_image.append(0)
            result.append(new_image)
        return result
    
    
s1 = Solution()
image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
print(s1.flipAndInvertImage(image))