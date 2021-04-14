
# =======================================================================================================================
# The Python split() method breaks up a string at the specified separator and
# and returns a list of strings

n = 'Tony.Angie.Will.Jaz.Kel.Emma'
name = n.split('.')
print(name)

# We can also use lists as a form of database.
# This following code snippet is an example

database = [
    ['Ali', 'Tony', 'Angie'],
    ['Kim', 'Li', "Li"],
    [23, 22, 25],
]

userName = database[0]
familyName = database[1]
age = database[2]

input1 = str(input('please enter user or password'))

# We can do queries on the database by writing a if construct
if input1 == 'f' or input1 == 'firstname':
    print(userName)
elif input1 == 'l' or input1 == 'lastname':
    print(familyName)
else:
    print(age)
