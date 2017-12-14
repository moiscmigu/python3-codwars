# Implement a function likes :: [String] -> String, which must take in input array, containing the
# names of people who like an item. It must return the display text as shown in the examples:

# likes [] // must be "no one likes this"
# likes ["Peter"] // must be "Peter likes this"

# For more than 4 names, the number in and 2 others simply increases.


def likes(name):
    lenOfArr = len(name)
    peopleWhoLikeIt = ""

    if lenOfArr >= 4:
        peopleWhoLikeIt = "%s, %s and %s others like this" % (name[0], name[1], lenOfArr - 2)

    elif lenOfArr == 0: #pass
        peopleWhoLikeIt = "no one likes this"

    elif lenOfArr == 1: #pass
        peopleWhoLikeIt = "%s likes this" % (name[0])

    elif lenOfArr == 3:
       peopleWhoLikeIt = "%s, %s and %s like this" %(name[0], name[1], name[2])

    else:
        peopleWhoLikeIt = "%s and %s like this" % (name[0], name[1])


    print(peopleWhoLikeIt)
    return peopleWhoLikeIt

