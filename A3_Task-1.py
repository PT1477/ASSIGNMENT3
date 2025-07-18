
def factorial(n):
    a = 1
    n=int(input("Enter a number: "))
    for i in range(1,n+1):
        a=a*i
    return a

p=factorial(5)
print(p)

