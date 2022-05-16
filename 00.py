def isPrime(number: int) -> bool:
    #all even numbers above 2 can't be prime
    if number > 3 and number % 2 == 0:
        return False
    # 0, 1, 2 and 3 are Prime
    if number in [0, 1, 2, 3]:
        return True

    for i in range(3, number):
        if i != number and number % i == 0:
            return False
    return True