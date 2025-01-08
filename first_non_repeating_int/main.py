def non_repeating_system(string:str) -> str:
        my_dict = {}
        for char in string:
            my_dict[char] = my_dict.get(char, 0) + 1
        

        # for key, value in my_dict.items():
        #     if value == 1:
        #         return string.index(key)

        for i in range(len(string)):
            # if my_dict[string[i]] == 1:
            #     return i
            print(my_dict[string[i]], string[i])
            


string = "leetcode"
# string = "loveleetcode"
print(non_repeating_system(string))
