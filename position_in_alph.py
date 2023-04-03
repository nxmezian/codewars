#https://www.codewars.com/kata/546f922b54af40e1e90001da/solutions/python

#replaces letters of the alphabet with their respective position in the alphabet

def alphabet_position(text):

  for i in text.lower():
      if i.isalpha():
          x = ord(i) - 96
          sentence += f"{x} "
   
   return sentence
