import math
from functools import reduce
text = open("input13.txt", "r").readlines()
time = int(text[0])
print(time)
buses = text[1].strip().split(",")
print(buses)
IDs = list()
for m in buses:
    try:
        IDs.append(int(m))
    except ValueError:
        continue
print(IDs)
vals = [a*b for a,b in zip(IDs, [math.ceil(time/i) for i in IDs])]
waitTime = min(vals)- time
myBus = IDs[vals.index(min(vals))]
print(waitTime, myBus, waitTime * myBus)

# Leo's Part 1 Solution trick
# i - n % i < dt: where i is the bus ID, n the time, and dt the current smallest wait time

# Part 2 (my implementation of Chinese Remainder Theorem)
N = reduce(lambda a,b: a*b, IDs)
t = 0
for i, b in enumerate(buses):
    if b != 'x':
        t += N/int(b)*(i)*()
print(N)



# Part 2: Solution completely from Leo Diperna
# Comment are my own for understanding

# n, incr = 0, -1
# for i in range(len(buses)):
#     if buses[i] != 'x':
#         if incr == -1:
#             incr = int(buses[i])
#             continue
#         while (n + i) % int(buses[i]) != 0:
#             n += incr
#         incr *= int(buses[i])
# print(n)