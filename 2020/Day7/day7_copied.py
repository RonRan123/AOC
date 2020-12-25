# from parse import *
#
# x = {search('{} bag', x)[0]: [*findall('{:d} {} bag', x)]
#         for x in open('input7.txt')}
#
# t = 'shiny gold'
#
# def f(c): return any(d==t or f(d) for _,d in x[c])
# def g(c): return sum(n + n * g(d) for n,d in x[c])
#
# print(sum(map(f, x)), g(t))


import collections
import math
import re
import sys
text= open('input7.txt').readlines()
lines = [l.rstrip('\n') for l in text]

containedin = collections.defaultdict(set)
contains = collections.defaultdict(list)
for line in lines:
    color = re.match(r'(.+?) bags contain', line)[1]
    print(re.match(r'(.+?) bags contain', line))
    print(re.findall(r'(\d+) (.+?) bags?[,.]', line))
    print()
    for ct, innercolor in re.findall(r'(\d+) (.+?) bags?[,.]', line):
        ct = int(ct)
        containedin[innercolor].add(color)
        contains[color].append((ct, innercolor))

# part 1:
# holdsgold = set()
# def check(color):
#     for c in containedin[color]:
#         holdsgold.add(c)
#         check(c)
# check('shiny gold')
# print(len(holdsgold))

def cost(color):
    total = 0
    for ct, inner in contains[color]:
        total += ct
        total += ct * cost(inner)
    return total
print(cost('shiny gold'))