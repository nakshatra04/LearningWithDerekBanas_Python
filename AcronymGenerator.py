from __future__ import print_function

input_string = raw_input("Enter your string : ")

input_string = input_string.upper()

word_list = input_string.split()

for word in word_list:
    print(word[0],end="")
