# Write a program which can compute the factorial of a given numbers. Use recursion to find it.
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

num=input('Enter a number:')
print fact(num)