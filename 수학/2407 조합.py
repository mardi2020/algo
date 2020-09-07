import sys
import operator as op
from functools import reduce
input = sys.stdin.readline

n, r = map(int, input().split())

if n-r < r :
    r = n-r

def ncr(n, r):
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer//denom


print(ncr(n, r))