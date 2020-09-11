"""
Peter wants to generate some prime numbers for his cryptosystem. Help him! Your task is to generate all prime numbers
between two given numbers!

Input
The input begins with the number t of test cases in a single line (t<=10). In each of the next t lines there are
two numbers m and n (1 <= m <= n <= 1000000000, n-m<=100000) separated by a space.

Output
For every test case print all prime numbers p such that m <= p <= n, one number per line, test cases separated by
an empty line.

Example
Input:
2
1 10
3 5

Output:
2
3
5
7

3
5
"""

t = int(input('Tests: '))

for _ in range(t):
    min_ = int(input('Min: '))
    max_ = int(input('Max: '))

    primes = []

    for num in range(min_, max_ + 1):
        dividers = 0

        for current in range(1, num + 1):
            if num % current == 0:
                dividers += 1
        
        if dividers == 2:
            primes.append(num)

    print(primes)
