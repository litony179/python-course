# =======================================================================================================================
# The Python input() method reads a line form input, converts it into a string and returns it to the console
print('please enter your name: ')
name = input()
print("hi " + name)
print("please enter your family name: ")
familyName = input('> ')
print('ok ' +  name + " " + familyName)

# =======================================================================================================================
# An integral part of any programing language is decision making.
# Decision making is required when we want to execute a code body only if a centratin condition is met.
# lets look a the "if" statement to do decision making.

print('enter your age ')
age = int(input())

# Note the spaces in the "if" construct, in python we do nothave curly places, instead we put a tab (4 spaces) to denote
# that we are in a construct body.

# This is an example of an "if...else" construct

if age > 18:
    print('you can enter!')
else:
    print('you can not enter!')

# This is an "if...elif...else" construct in Python
if age < 18:
    print('This is licenced venue, underage personel are prohibited')
elif age > 18 and age < 35:
    print("welcome to our bar!")
elif age > 60:
    print("You're so old to enter!")
else:
    print('enter your age: ')

