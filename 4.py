"""
Transform the algebraic expression with brackets into RPN form (Reverse Polish Notation).
Two-argument operators: +, -, *, /, ^ (priority from the lowest to the highest), brackets ( ).
Operands: only letters: a,b,...,z. Assume that there is only one RPN form (no expressions like a*b*c).

Example
Input:
3
(a+(b*c))
((a+b)*(z+x))
((a+t)*((b+(a+c))^(c+d)))

Output:
abc*+
ab+zx+*
at+bac++cd+^*
"""

input_ = '((a+t)*((b+(a+c))^(c+d)))'
plus = ''
mul = ''
pow_ = ''


for c in input_:
    if c == '+':
        plus += '+'
    if c == '*':
        mul += '*'
    if c == '^':
        pow_ += '^'

input_ = input_.replace('+', '').replace('*', '').replace('^', '').replace('(', '').replace(')', '')

output = input_ + plus + mul + pow_

print(output)
