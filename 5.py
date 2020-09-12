"""
A positive integer is called a palindrome if its representation in the decimal system is the same when
read from left to right and from right to left. For a given positive integer K of not more than 1000000 digits,
write the value of the smallest palindrome larger than K to output. Numbers are always displayed without leading zeros.

Input
The first line contains integer t, the number of test cases. Integers K are given in the next t lines.

Output
For each K, output the smallest palindrome larger than K.

Example
Input:
2
808
2133

Output:
818
2222
"""

t = int(input('t: '))

for _ in range(t):
    k = int(input('k: '))

    current = k + 1

    while str(current) != str(current)[::-1]:
        current += 1

    print(current)
