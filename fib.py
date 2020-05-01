stack={}

def fib(n):
    if n in stack:
        return stack[n]
    elif n==0 or n==1:
        return 1
    else:
        stack[n]=fib(n-1)+fib(n-2)
        return stack[n]