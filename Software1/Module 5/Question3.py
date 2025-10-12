n = int(input("Enter an integer: "))
if n < 2:
    print(f'{n} is not a prime number.')
else:
    isprime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            isprime = False
    if isprime:
        print(f'{n} is a prime number.')
    else:
        print(f'{n} is not a prime number.')
