n = int(input())

count = 0
count2 = 1

fib = list()
fib.append(count)

while n > len(fib):
    seq = count + count2
    fib.append(seq)
    if n > len(fib):
        count = count2 + seq
        fib.append(count)
        if n > len(fib):
            count2 = seq + count
            fib.append(count2)
print(*fib)