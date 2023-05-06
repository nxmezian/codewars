# https://www.codewars.com/kata/6402205dca1e64004b22b8de/solutions/python

def find_caterer(budget, people):

    if people <= 0:
        return -1

    if people > 60:
        if budget >= people * 24:
            return 3

    if people * 15 <= budget and budget <= people * 20:
        return 1

    elif people * 20 <= budget and budget <= people * 30:
        return 2

    elif people * 30 <= budget:
        return 3
    else:
        return -1
