#https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/python

#returns initials

def abbrev_name(name):
    name = name.upper().split(" ")
    return f"{name[0][0]}.{name[1][0]}"
