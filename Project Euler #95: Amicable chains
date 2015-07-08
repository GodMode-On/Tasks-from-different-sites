from functools import reduce
from operator import mul
import time
start_time = time.time()


n = 100000

def factorization(n):
    """
    Generate the prime factorization of n in the form of pairs (p, k)
    where the prime p appears k times in the factorization.
    """
    p = 1
    while p * p < n:
        p += 1
        k = 0
        while n % p == 0:
            k += 1
            n //= p
        if k:
            yield p, k
    if n != 1:
        yield n, 1
        
def divisor_gen(n):
    """
    Generate all divisors of a number(including entire number!)
    """
    factors = list(factorization(n))
    nfactors = len(factors)
    f = [0] * nfactors
    while True:
        yield reduce(mul, [factors[x][0]**f[x] for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= factors[i][1]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return


def check(n):
    divs = [0 for i in range(1000001)]
    max_set = set()
    len_max_set = 0
    for number in range(6,n+1):
        if not divs[number]:
            divs[number] = sum(divisor_gen(number)) - number
        SOD = divs[number]
        numbers = set()
        while True:
            if SOD == 1 or SOD > n:
                numbers = set()
                break
            elif SOD in numbers:
                if number in numbers:
                    if len(numbers) > len_max_set:
                        max_set = numbers.copy()
                        len_max_set = len(max_set)
                    elif len(numbers) == len_max_set:
                        max_set |= numbers
                break
            else:    
                numbers |= {SOD}
                if not divs[SOD]:
                    divs[SOD] = sum(divisor_gen(SOD)) - SOD
                SOD = divs[SOD]
    return min(max_set)



print (check(n))
print("--- %s seconds ---" % (time.time() - start_time))
