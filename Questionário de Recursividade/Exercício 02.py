def fibonacci(n, a=0, b=1, count=0):
    if count < n:
        print(a, end=" ")
        fibonacci(n, b, a + b, count +1)