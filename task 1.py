n=int(input("eneter a number "))
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(f"the factorial of {n} is {factorial(n)}")
