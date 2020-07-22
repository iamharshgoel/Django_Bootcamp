#####################################
#### PART 6: EXERCISE REVIEW  #######
#####################################

# Time to review all the basic data types we learned! This should be a
# relatively straight-forward and quick assignment.

###############
## Problem 1 ##
###############

# Given the string:
s = 'django'
print(s[0])
print(s[-1])
print(s[0:4])
print(s[1:4])
print(s[4:])

# Use indexing to print out the following:
# 'd'

# 'o'

# 'djan'

# 'jan'

# 'go'

# Bonus: Use indexing to reverse the string


###############
## Problem 2 ##
###############

# Given this nested list:
l = [3,7,[1,4,'hello']]
# Reassign "hello" to be "goodbye"
l[2][2] = "goodbye"
print(l)


###############
## Problem 3 ##
###############

# Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key':'hello'}

d2 = {'k1':{'k2':'hello'}}

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print(d1['simple_key'])
print(d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1])

###############
## Problem 4 ##
###############

# Use a set to find the unique values of the list below:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
z = set(mylist)
print(z)


###############
## Problem 5 ##
###############

# You are given two variables:
age = 4
name = "Sammy"
print("Hello my dog's name is {} and he is {} years old".format("Sammy",4))

# Use print formatting to print the following string:
"Hello my dog's name is Sammy and he is 4 years old"
