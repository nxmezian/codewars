#https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python
def digitize(n):
    return [int(i) for i in str(n)[::-1]]

def digitize2(n):
    num_array = [] # make empty array
    for number in str(n): # make n into string to interate through
        num_array.insert(0, int(number)) # insert number into 1st position (reverses it)
    return num_array # return array

print(digitize(321246))