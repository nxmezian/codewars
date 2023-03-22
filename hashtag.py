#https://www.codewars.com/kata/52449b062fb80683ec000024/train/python

#creates valid hashtag based on input
def generate_hashtag(s):

    #hashtag cannot be zero characters after the hash
    if s == "":
        return False

    s = s.split()

    hash_tag = "#"

    for i in s:
        i = i.capitalize()
        hash_tag += i

    if len(s) > 140:
        return False
    else:
        return hash_tag


print(generate_hashtag("Hello there thanks for trying my Kata"))