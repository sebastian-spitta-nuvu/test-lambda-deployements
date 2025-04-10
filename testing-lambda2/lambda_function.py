def prime_number(x):
    for n in range(2,x):
        if x%n == 0:
            return False
    return True
