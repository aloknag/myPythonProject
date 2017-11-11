x = 2
number_of_primes = 0
primes = []


def is_prime(x):
    for y in range(1, x):
        if x % y == 0 and y != 1:
            return False
    return True


while number_of_primes < 1000:
    if is_prime(x):
        number_of_primes += 1
        primes.append(x)
    x += 1

row = 0
col = 0
while row + col < 1000:
    if col < 10:
        print "%4d   " % primes[row+col],
        col += 1
        if col == 10:
            print "\n"
            col = 0
            row = row + 10


