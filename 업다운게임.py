
정답 = 80

while True:
    a = int(input("숫자를 입력하세요:"))
    if a == 정답:
        print("정답입니다.")
        break
    elif a > 정답:
        print("다운")
    elif a < 정답:
        print("업")
    else:
        print("입력한 수를 다시 확인 해주세요")




