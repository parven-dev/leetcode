class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        
        my_list = []
        checkList = []
        for item in letters:
            my_list.append(ord(item))
        
        for num in sorted(my_list):
        
            if num > ord(target):
                checkList.append(chr(num))
        
        if len(checkList) == 0:
            return chr(my_list[0])

        return (checkList[0])

s1 = Solution()
letters = ["x","x","y","y"]
target = "z"

print(s1.nextGreatestLetter(letters, target))