# Write a function that returns both the minimum and maximum number of the given list/array.
#
# Examples
# min_max([1,2,3,4,5])   == [1,5]
# min_max([2334454,5])   == [5, 2334454]
# min_max([1])           == [1, 1]


def min_max(lst):

    min = lst[0]
    max = lst[0]

    for item in lst:

        # will find the smallest int
        if min >= item:
            min = item

        if max <= item:
            max = item

    sortedList = [min, max]

    return sortedList


min_max([1,1])

