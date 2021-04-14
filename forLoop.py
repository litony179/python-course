# =======================================================================================================================
# the Python 'for' loop is used to iterate over a sequence (list, tuple, string) or other iterable objects
# Iterating is also known as traversing

# Note, the range() method generates a sequence of numbers.
# range(10) will generate numbers from 0 to 10
for i in range(10):
    print(i)

# =======================================================================================================================
# This is an example working with lists

myList = [0,1,2,3,4,5,6,7]
for i in myList:
    print(i + 2)
    print('Tony')

# =======================================================================================================================
# Another for loop example

genre = ['pop', 'rock', 'classic']
for i in range(len(genre)):
    print('I like to listen to ' + genre[i])