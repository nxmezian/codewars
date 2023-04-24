#https://www.w3schools.com/python/ref_string_isnumeric.asp

def high_and_low(numbers):
    unsorted_list = []
    for i in numbers:
        if i.isnumeric():
            unsorted_list.append(int(i))

    unsorted_list.sort()
    for i in numbers:
        if i.isnumeric():
            if i



print(high_and_low("3,4,5,1"))  # return "5 1"