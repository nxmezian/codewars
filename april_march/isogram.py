#https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python

#Checks if string is an isogram, i.e. every letter is unique 

def is_isogram(string):
    test_string = {}
    for i in string.lower():
        if i in test_string:
            return False
        else:
            test_string[i] = 1
    return True

