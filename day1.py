def reader(folderName) :
    with open(folderName,encoding="utf-8") as f: 
        data = f.read()
    return data 

input_day_one = reader("day1.txt")

print(type(input_day_one))

print(input_day_one)


def day_one_first_star(input) :
    counter = 0
    for ch in input:
        if(ch == "("): 
            counter+=1 
        elif (ch == ")"): 
            counter-=1 
        else: 
            continue 
    return counter 


resultDayOne = day_one_first_star(input_day_one)


def day_one_second_star(input_text):
    counter = 0
    position = 0
    for ch in input_text:
        position += 1
        if ch == "(":
            counter += 1
        elif ch == ")":
            counter -= 1
        if counter == -1:
            return position

print(day_one_first_star(input_day_one))
print(day_one_second_star(input_day_one))





