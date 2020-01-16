# Square all even numbers from 10 to 20. Print the result. The beginning and end of
# the list are entered from the console

number = int(input('Enter number: '))
number2 = int(input('Enter number 2: '))

if number % 2 != 0:
    number += 1

if number2 < number:
    print("Enter valid value ")
for i in range(number, number2+1, 2):

    print(i, i**2)

