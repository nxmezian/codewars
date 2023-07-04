#https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python

def find_it(seq):
    count = {}
    for i in seq:
        if i not in count:
            count[i] = 1
        else:
            count[i] +=1
    
    for c in count:
        if count[c] % 2 != 0:
            return(c)
        

print(find_it([1,1,2]))