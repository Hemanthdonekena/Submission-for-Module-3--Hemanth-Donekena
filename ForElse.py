for num in range(10, 20):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            j = num // i
            print('{} equals {} * {}'.format(num, i, j))
            is_prime = False
            break
    if is_prime:
        print(num, 'is a prime number')
