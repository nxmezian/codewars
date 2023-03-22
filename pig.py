#https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python
import string

def pig_it(text):
    text = text.split()
    pig_text = {}

    for i in text:
        pig = ""
        pig = pig + i[1:] + i[0] + "ay"
        pig_text += pig

    return pig_text


print(pig_it("heey how you doin"))
