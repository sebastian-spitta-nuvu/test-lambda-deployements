def prime_number(x):
    for n in range(2,x):
        if x%n == 0:
            print("Hola mundo desde la primera lambda :D")
            return False
    return True
