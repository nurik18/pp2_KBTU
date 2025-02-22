import re

string = 'abb'
#1
pattern = re.fullmatch(r'ab*', string)
if pattern:
    print("True")
else: 
    print("False")


#2 
string = 'abb'
pattern = re.fullmatch(r'ab{2,3}', string)

if pattern:
    print("True")
else:
    print("False")


#3 
string = 'snake_case'

pattern = r'[a-z]*\_*'

if pattern:
    print("True")
else:
    print("False")

#4
