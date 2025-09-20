def reader(folderName) :
    with open(folderName,encoding="utf-8") as f: 
        data = f.read()
    return data 

input_day_one = reader("day1.txt")

print(type(input_day_one))

print(input_day_one)


def day_one(input) :
    counter = 0
    for ch in input:
        if(ch == "("): 
            counter+=1 
        elif (ch == ")"): 
            counter-=1 
        else: 
            continue 
    return counter 


resultDayOne = day_one(input_day_one)

print(type(resultDayOne))
print(resultDayOne)
