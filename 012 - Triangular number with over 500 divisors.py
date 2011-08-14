# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
# The first ten terms would be:
#  1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# Let us list the factors of the first seven triangle numbers:
#
#     1: 1
#     3: 1,3
#     6: 1,2,3,6
#    10: 1,2,5,10
#    15: 1,3,5,15
#    21: 1,3,7,21
#    28: 1,2,4,7,14,28
#
# We can see that the 7th triangle number, 28, is the first triangle number
# to have over five divisors.
#
# Which is the first triangle number to have over five-hundred divisors?


# N.B. The nth triangular number is give by n*(n+1)/2
import math, time

def count_factors(K):
    factors = 2 # include 1 and K
    for i in xrange(2, math.floor(math.sqrt(K) + 1)):        
        if (K % i == 0):
            if (i**2 == K): # don't count sqrt twice.
                factors += 1
            else:
                factors += 2
    return factors

def factor(K):
    factors = []
    for i in xrange(2, math.floor(math.sqrt(K) + 1)):        
        if (K % i == 0):
            factors.append(i)
            other = K / i            
            if (other != i):
                factors.append(other)
    factors.sort()
    return factors

def prime_factor(K):
    primes = []
    for k in factor(K):   
        if (len(factor(k)) == 0):
            primes.append(k)
    primes.sort()
    return primes

start_time = time.time()
# Might as well start where the example leaves off (incredibly minor optimization)
i = 7
triangular = 28
while (True):
    i += 1
    triangular += i
    factors = count_factors(triangular)
    if (factors > 500):
        print i, " ", triangular
        break

print "Elapsed Time: ", time.time() - start_time, "second(s)"  # = 10.7(s)
# 12375th triangular number, which is: 76,576,500

# From Landon:
# Let N(x) be the number of factors of x.
# Now, it is almost true that N(ab) = N(a)N(b), but not quite, because there can be interference.
# It is true that if a and b have no primes in common (their gcd is 1 in other words)
# then N(ab) = N(a)N(b). We can use this fact to get a formula for the number of factors of x
# in terms of its prime factorization.
# Note that if p is prime then N(p^k) = k + 1.
# Say x = p_1^k_1 * p_2^k_2 * ... * p_n^k_m, for distinct primes p_i.
# Then N(x) = N(p_1^k_1 * p_2^k_2 * p_n^k_m) = (k_1 + 1) * (k_2 + 1) * ... *(k_m + 1)
# So x = p_1^k_1 * p_2^k_2 * ... * p_n^k_m
# Which means we need (k_1 + 1) * (k_2 + 1) * ... *(k_m + 1) > 500,
# minimizing p_1^k_1 * p_2^k_2 * ... * p_n^k_m
# That will give us > 500 factors. We'll still have to make sure the number is triangular at the end.
# 500 = 2^2 * 5^3, so the ki's are either 1 or 4, and there are 2 1's, and 3 4's
# or the ki could be 24 or 124 as well but I think those will generate numbers larger than we want.
# 2^124 * 3^3 has 500 factors

# Test for triangular numbers Tn = n(n+1) / 2.
# Given T, let n be floor(sqrt(T)). if T == n(n+1) / 2, then T is triangular.