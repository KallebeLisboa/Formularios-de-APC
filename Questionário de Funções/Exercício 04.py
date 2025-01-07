def nota(n):
    print("|", end = "")
    for c in range (n):
        print("★", end = "")
    for c in range(10-n):
        print("☆", end = "")
    print("|")
