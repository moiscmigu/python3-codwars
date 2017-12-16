# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
#
# Example:
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
#
# The returned format must be correct in order to complete this challenge.
# Don't forget the space after the closing parenthesis!




def create_phone_number(n):

    myArr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    if len(n) != 10:
        print("You need to enter 10 Digits")
        return None
    else:


        formatedString = "({f[0]}{f[1]}{f[2]}) {f[3]}{f[4]}{f[5]}-{f[6]}{f[7]}{f[8]}{f[9]}".format(f=n)
        return formatedString
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])