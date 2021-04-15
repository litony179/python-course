# =====================================================================================================
# This following code snippet demonstrate using a if construct and a for loop to check if a list is
# Empty or not.
list = []
if len(list) == 0:
    print('There is nothing in the list')
else:
    for i in list:
        print(i)

# =====================================================================================================
# We can also to form checks to see if a user has actually entered a namne into the field.

name = str(input('please enter your name'))
if name != None:
    print(name)
else:
    print('please enter your name again')

# =====================================================================================================
# We can also check of a username is in a database

nameEntry = str(input("please enter your name"))
userName = ["Tony", 'Ali', "Angie"]
if nameEntry not in userName:
    print('This user name does not exist in our database')
    print('but we will add you onto our database')
    print('welcome {}'.format(nameEntry))
    userName.append(nameEntry)
    print(userName)
else:
    print('welcome {}'.format(nameEntry))
