#https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python

#Checks if the number of "x" and "o" is equal i
def xo(s):
    count = {"x":0, "o":0}

    for i in s.lower():
        if i =="x" or i == "o":
            count[i] +=1

    if count["x"] == count["o"]:
        return True
    else:
        return False
