def convert(s):    
    for item in range(len(s) //2):
        left = item
        right = len(s)-1 - item
        temp = s[left]
        s[left] = s[right]
        s[right] = temp        
         
    return s
s = ["h","e","l","l","o"]
print(convert(s))