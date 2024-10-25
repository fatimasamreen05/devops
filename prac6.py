#6.Write a python program to find factorial of a number using function recursion.
def factorial(n)->int:
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

num=int(input("enter number"))
result = factorial(num)
print(result)

