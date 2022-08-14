dan = int(input("원하는 단 입력 : "))
if dan <= 10 and dan >= 1:
    for i in range(1, 10):
        print("{} * {} = {}".format(dan, i, dan*i))
else:
    print("1~9 범위의 정수를 입력해주세요")
1