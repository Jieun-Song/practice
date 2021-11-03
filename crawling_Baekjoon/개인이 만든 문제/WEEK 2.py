#백준 10800

n = int(n)
color = []
big = []

for i in range(n):
    c, b = input().split()
    c = int(c)
    b = int(b)
    color.append(c)
    big.append(b)


for i in range(n):
    sum = 0
    for m in range(n):
        if i != m and color[i] != color[m] and big[i] > big[m]:
            sum += big[m]
    print(sum)
