


def reader(folderName) :
    with open(folderName,encoding="utf-8") as f: 
        data = f.read()
    return data 

input_day_one = reader("day1.txt")

print(type(input_day_one))

print(input_day_one)
