value = input('Enter a natural number: ')

if value.isdigit():
    value = int(value)
    reciprocal = 1 / value
    print('The reciprocal of', value, 'is', reciprocal)
else:
    print("Cannot take the reciprocal of a non-integer value.")


if type(value) is int:
    print("The input was an integer.")
