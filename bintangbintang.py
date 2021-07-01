def stars (n):
    for i in range(0,2 * n + 1):
        if i < n:
            print("*" * (n-i))
        elif i != n:
            print("*" * (i-n))
            
stars(20)
