# Exercise 11. Check Primality Functions
#
# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten,
# a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to
# help you. Take this opportunity to practice using functions, described below.


def odd_even():
    num = int(input("Hello, please enter a number: "))
    if num % 2 == 0:
        print("Your number it's even")
    else:
        print("Your number it's odd")


odd_even()
