n = 1
while n <=100:
    if n % 10 == 0:
        print(n)
    else:
        print(n,end ='\t')
    n += 1
print("=======================================")

for i in range(1,101):
    if i % 10 == 0:
        print(i)
    else:
        print(i,end ='\t')
    i += 1