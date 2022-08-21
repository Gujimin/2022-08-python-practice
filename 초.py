입력 = int(input("초를 입력하세요>>>"))
second = 입력 % 60
minute = (입력 % 3600) // 60
hour = 입력//3600
print("변환 결과는 {}시간  {}분 {}초 입니다.".format(hour,minute,second))