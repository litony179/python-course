# =====================================================================================================
# We can do operations on each elements of a list though the use of loops
# Here is an example where we square every element in the list and put it into a new list

numbers = [0,1,2,3,4,5,6,7,8,9,10]
squareNumbers = []

for i in numbers:
    m = i ** 2
    print(m)
    squareNumbers.append(str(m))
    print(squareNumbers)

# =====================================================================================================
# We can also do linear search on a list with a for loop
# Here is an example where we try to find the max number in a list
# Time complexity is O(n)

numbers2 = [3,6,4,7,3,5,7,83,73,57,57,568,5686,4,124983]
for i in numbers2:
    max = numbers2[0]
    if(i > max):
        max = i
print('the max number in the list is {} '.format(max))


# Python provides a built in method for finding the max and min element in a list
# here is an example
minimum = [1,2,3,46,57,58,35635,367,7457,45,63,523,5]
small = min(minimum)
print('the minimum number in "minimum" list is {} '.format(small))

# =====================================================================================================
# This is an example where we find the total sum of a list

numbers3 = [3,57,34,65,7,347,57,65,745,75,64,634,4,325]
sum = 0
for i in numbers3:
    sum = sum + i
print('the sum of the "numbers3" list is {} '.format(sum))

# there is also a Python built in method sum() that achieves the same thing as the above code
addingList1 = [4,67,4,74,3,6,57,46,6,68,35]
print(sum(addingList1))