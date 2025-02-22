class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        
        fizz_buzz_list = []
        for item in range(1, n+1):
            if item % 3 == 0:
                fizz_buzz_list.append("Fizz")
            if item % 5 == 0:
                fizz_buzz_list.append("Buzz")
            if item % 5 == 0 and item % 3 == 0:
                fizz_buzz_list.append("FizzBuzz")
            else:
                fizz_buzz_list.append(item)
                
        return fizz_buzz_list
                
                
    
    
s1 = Solution()
n = 15
print(s1.fizzBuzz(n))

        