#https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/solutions/python

#checks for valid PINs: 4 or 6 digit numbers only
def validate_pin(pin):
    import re

    if re.fullmatch(r"^\d{4}$", pin) or re.match(r"^\d{6}$", pin):
        return True
    else:
        return False
