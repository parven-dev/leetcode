
def power(data):
    sets = set()
    while data != 1 and data not in sets:
        sets.add(data)   
        data = sum(pow(int(i), 2) for i in str(data))
    return data == 1   


data = 19
print(power(data))  