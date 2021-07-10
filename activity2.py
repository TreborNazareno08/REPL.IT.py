# cabitac, vriohn trebor n.
import string

letter_string = string.ascii_uppercase
letter_list = list(letter_string)

while True:
    var = int(input("Enter a number between 0 and 35 "))
    b = list(range(var, 36))
    if 9 < var < 36:
        for x in range(var - 10, len(letter_list)):
            print('{} for {}'.format(letter_list[x], x + 10))
    else:
        print(var)
        break
