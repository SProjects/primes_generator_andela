def primes_generator(limit):
    if not isinstance(limit, int):
        raise ValueError('Limit values must be an integer')

    if limit < 2:
        raise ValueError('Limit values should be greater then 1')

    results = []
    for number in range(2, limit + 1):
        is_prime = True
        divisor = 2
        while divisor < number:
            if number % divisor == 0:
                is_prime = False
            divisor += 1

        if is_prime:
            results.append(number)

    return results

