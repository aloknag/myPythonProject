x = 2
numberofprimes = 0
primes = []


def isPrime(x):
    for y in range(1, x):
        if x % y == 0 and y != 1:
            return False
    return True


while numberofprimes < 1000:
    if isPrime(x):
        numberofprimes += 1
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
            col = 0;
            row = row + 10


