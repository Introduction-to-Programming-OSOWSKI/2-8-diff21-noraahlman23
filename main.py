def diff21(n):
    if n < 21:
        return abs (n-21)
    elif n > 21:
        return (abs (n-21)) * 2
    else:
        return 0

print (diff21(25))