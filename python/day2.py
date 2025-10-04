def reader(foldername): 
    with open(foldername, encoding="utf-8") as f:
        data = f.read().splitlines()
    return data


def calc(params):
    a, b, c = map(int, params)
    min_num = min(a*b, b*c, a*c)
    nums = 2*(a*b + b*c + a*c)
    return min_num + nums


def calc_day_two(params): 
    a, b, c = sorted(map(int, params))
    wrap = 2 * (a + b)
    bow = a * b * c
    return wrap + bow


def day_two(input_list): 
    arr = []
    counter = 0
    for item in input_list: 
        array = item.split("x")      
        arr.append(array)
    for dims in arr:                 
        counter += calc_day_two(dims)        
    return counter


input_day_two = reader("../day2.txt")



print(day_two(input_day_two))



