class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        seats = sorted(seats)
        students = sorted(students)
        sums = 0
        
        for i in range(len(seats)):
            # print(seats[i], students[i])
            # sums+=(seats[i]) - (students[i])
            total_left = (students[i] - seats[i])
            sums+=(abs(total_left))
        
        return sums
    
    
  
s1 = Solution()
  
# seats = [3,1,5]
# students = [2,7,4]
seats = [12,14,19,19,12]
students = [19,2,17,20,7]

print(s1.minMovesToSeat(seats, students))
    