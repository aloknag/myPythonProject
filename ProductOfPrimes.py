from math import log, e


class GetPrimes:
    """ For a given number m has method to generate primes till m"""
    def __init__(self, m):
        self.primes = self.generate_primes(m)

    def __str__(self):
        return str(self.primes)

    def is_prime(self, x):
        for y in range(1, x):
            if x % y == 0 and y != 1:
                return False
        return True

    def generate_primes(self, m):
        p = []
        for x in range(2, m):
            if self.is_prime(x):
                p.append(x)
        return p

    def find_log(self, num):
        return log(num)

    def sum_of_log_n(self):
        log_of_primes = map(self.find_log, self.primes)
        return sum(log_of_primes)


if __name__ == "__main__":
    n = input('Enter a large number: ')
    primes = GetPrimes(n)
    sum_of_log_of_primes = primes.sum_of_log_n()
    ratio = float(sum_of_log_of_primes / n)
    print "The sum of log of primes = %d" % sum_of_log_of_primes
    print "The ratio is = %f" % ratio
    print "is it close to %f" % log(e)