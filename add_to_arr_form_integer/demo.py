class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        i = len(num) - 1  # Start from the last digit
        carry = k
        result = []
        
        while i >= 0 or carry > 0:
            if i >= 0:
                carry += num[i]  # Add the digit to carry
                i -= 1
            
            result.append(carry % 10)  # Extract last digit
            carry //= 10  # Reduce carry
            
        return result[::-1]  # Reverse to get correct order

# Example Usage
s1 = Solution()
num = [1,2,0,0]
k = 34
print(s1.addToArrayForm(num, k))
