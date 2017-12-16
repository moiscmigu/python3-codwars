# You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.
#
# Examples
# [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)
#
# [160, 3, 1719, 19, 11, 13, -21]
# Should return: 160 (the only even number)


def checkListType(list):

    odd = 0
    even = 0

    for numbers in list:

        # check if it is even
        if numbers %2 == 0:
            even += 1
        # check if it is odd
        else:
            odd += 1

    if odd > even:
        return "odd"
    else:
        return "even"

def find_outlier(integers):

    alienInt = int

    listType = checkListType(integers)

    # Will try to find the odd number
    if listType == "even":

        for numbers in integers:

            if numbers % 2 != 0:
                alienInt = numbers
                break
    else:

        for numbers in integers:

            if numbers % 3 != 0:
                alienInt = numbers
                break

    print("This is what i am returning: {}".format(alienInt))

    return alienInt


find_outlier([160, 3, 1719, 19, 11, 13, -21])