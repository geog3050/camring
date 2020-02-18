###################################################################### 
# Edit the following function definition, replacing the words
# 'name' with your name and 'hawkid' with your hawkid.
# 
# Note: Your hawkid is the login name you use to access ICON, and not
# your firsname-lastname@uiowa.edu email address.
# 
# def hawkid():
#     return(["Caglar Koylu", "ckoylu"])
###################################################################### 
def hawkid():
    return(["Cameron Ring", "camring"])

###################################################################### 
# Problem 1 (25 Points)
# 
# Specification: listAverage(l) takes a list of numbers, l, and
# returns the average of these numbers. If the list is empty, it 
# returns False.
#
# For example:
#     >>> listAverage([])
#     False
#     >>> listAverage([1, 2, 3, 4, 5])
#     3.0
#     >>> listAverage([22, 30, 40])
#     30.666666666666668
#     >>> listAverage([23])
#     23.0
#     >>> listAverage([-24, -22, -13.123, 35.4])
#     -5.93075
# 
# Hint: remove the second line, which reads simply "pass," and
# replace it with the appropriate return() statement.
###################################################################### 
def listAverage(l):
    if l == False:
        print('False')
###################################################################### 
# Problem 2 (25 Points)
# 
# Specification: str2float(s) takes a string, s, as an argument. It
# returns 0.0 if s is an empty string. It returns False if the string 
# cannot be coverted to float data type. If s can be converted to 
# float data type, it returns the float value.
# 
# Hint: Consider using exception handling.
# 
# For example:
#     >>> str2float('abdcd')
#     False
#     >>> str2float('10.2')
#     10.2
#     >>> str2float('10,2')
#     False
#     >>> str2float('')
#     0.0
###################################################################### 
def str2float(s):
    pass

######################################################################
# Problem 3 (25 points)
# 
# Specification: lineLength(p1, p2) takes two arguments, p1 and p2,
# where both of them are points in 2D. Each point is a tuple where
# the coordinates are represented as (x, y). Therefore, the data
# structure for points is:
# - p1 = (x1, y1)
# - p2 = (x2, y2)
# 
# By default, the points are set to the origin point (0, 0).
# 
# The function returns the length of the line defined with given
# two points, p1 and p2.
# 
# For example:
#     >>> lineLength((10.2, 24.78), (33, 33.88))
#     24.548930730278254
#     >>> lineLength((22, 13), (25, 9))
#     5.0
#     >>> lineLength((6, 8))
#     10.0
#     >>> lineLength(p2=(14, -13.3))
#     19.31035991378721
#     >>> lineLength()
#     0.0
######################################################################
def lineLength(p1=(0, 0), p2=(0, 0)):
    pass

######################################################################
# Problem 4 (25 Points)
# 
# Specification: isOdd(n) takes an integer, n, and returns True if
# n is odd (i.e., not evenly divisible by 2) and False if the n is
# even (i.e., evenly divisible by 2).
# 
# For example:
#     >>> isOdd(42)
#     False
#     >>> isOdd(13)
#     True
###################################################################### 
def isOdd(n):
    pass

######################################################################
# MAKE NO CHANGES BEYOND THIS POINT.
######################################################################
if __name__ == '__main__' and hawkid()[1] == "hawkid":
    print('### Error: YOU MUST provide your hawkid in the hawkid() function.')
    print('### Otherwise, the Autograder will assign 0 points.')
