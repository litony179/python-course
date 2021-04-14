
# This file introduces the basics of Python lists
# The methods introduced here are all built into the Python language
# ================================================================================================================
# List indexes start from 0 (same as Java)
list1 = ['tony', 'ali', 'john', 'sarah']

# ================================================================================================================
# you can access individual items in a Python list by index calling
a = list1[0]
b = list1[1]
c = list1[2]
d = list1[3]
print(a,b,c,d)

# ================================================================================================================
# the title() function turns the first letter in each word in a particular string to capital letter
name = a.title()
print(name)

# ================================================================================================================
# in Python, negative indexing countes the elements from the end of the list to the first
# A used case for using this kind of indexing is to access the last element in a list(array).
lastElement = list1[-1]
print(lastElement.title())

# ================================================================================================================
# the len() function tells us the length of the list
lengthOfList = len(list1)
print(lengthOfList)

# ================================================================================================================
# We can also append(add) elements to the end of list by using the append() method
addElement = list1.append('whitney')
print(list1)

# ================================================================================================================
# We can also specify where to insert an element specifically
addToIndex0 = list1.insert(2, "Mark")
print(list1)

# ================================================================================================================
# To remove a element from a list, we can use the remove() method
# Note: The element that we remove when calling the remove() method will dissapear and does not ge  saved
remove2Index = list1.remove('Mark')
print(list1)

# ================================================================================================================
# To access the removed element, we can use the pop() method
# the pop() method 'pops'(deletes) off the specified element from the said list and temporarialy stores
# the deleted value

pop2Element = list1.pop(2)
print(list1)
print(pop2Element)