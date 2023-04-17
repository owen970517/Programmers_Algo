

import sys
n,m = sys.stdin.readline().split()

print(int(n.replace('6','5'))+ int(m.replace('6','5')) , int(n.replace('5','6')) + int(m.replace('5','6')))