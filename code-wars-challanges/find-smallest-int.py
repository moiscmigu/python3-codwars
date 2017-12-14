# Given an array of intergers your solution should find the smallest integers


myArr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 90, 34]
mySecondArr = [234, 23, 756, 2,34, 9, 96, 24, 1, 1, 2]


def findSmallestInt(arr):

    # By default the smallest int will always be the first number in the array

    smallestInt = arr[0]
    for index in arr:

        # Checks to see if the current smallest index is greater then the current index of the loop
        if smallestInt > index:

            # Will run if the index is smaller then what is assigned to the smallestInt
            smallestInt = index

    return smallestInt

