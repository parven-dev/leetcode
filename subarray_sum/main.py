class SubArraySum:
    def __init__(self, arr, target):
        self.arr = arr
        self.target = target
        
    
    def sum_array(self):
        # my_dict = {arr[item]: item for item in range(len(arr))}
        
        my_hash = {0:-1} 
                
        sums = 0
        
        for item in range(len(arr)):
            
            sums+=arr[item]
            
            data = sums - target 
            
            if data in my_hash:
                print(my_hash)
                return [my_hash[data] +1, item]
            
                # return [start_index = my_hash[sums - target] + 1, i]
                
                # return [start_index, item]
        
            my_hash[arr[item]] = item

            
        return []
    

        # for item in range(len(arr)):
        #     my_dict[arr[item]] = item
        #     # if target != sums :
        #     #     sums+=my_dict[arr[item]]
        #     #     data.append(my_dict[arr[item]])
        #     # else:
        #     #     return 
        # # return [data[0], data[-1]]
        
            
         
        
        
        
    


arr = [1,2,3,4,5]
target = 9
s1 = SubArraySum(arr, target)


print(s1.sum_array())