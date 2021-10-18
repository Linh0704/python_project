n = int(input())
p = 0
for i in range(10000000):
    p += 4*(((-1)**i)/(2*i+1))

Pi = p

print(str(Pi)[:n+2])
