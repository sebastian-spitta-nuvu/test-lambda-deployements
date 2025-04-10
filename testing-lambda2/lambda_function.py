def prime_number(x):
    for n in range(2,x):
        if x%n == 0:
            print("HOla mundo!!")
            return False
    return True
