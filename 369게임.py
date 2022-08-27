for i in range(1,100):
    a = i % 10
    b = i //10
    c = a % 3 == 0 and a != 0
    c1 = b % 3 == 0 and b != 0
    if c and c1:
        print('짝짝',end='\t')
    elif c or c1:
        print('짝',end='\t')
    else:
        print(i,end='\t')
    if i % 10 == 0:
        print()