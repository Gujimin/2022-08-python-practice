for i in range(2,10):
    if i % 2 == 0:
        continue
    for x in range(1, 10):
        print("{} * {}= {}".format(i, x, i * x))
        if i == x:
            break
else:
    print()
