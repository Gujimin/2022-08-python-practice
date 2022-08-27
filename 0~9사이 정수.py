a = []
while True:
      b = input("0~9 사이 정수를 입력하세요>>>")
      a.append(b)
      if len(set(a)) == 5:
          break

print("모두 입력되었습니다")
print("입력된 값은{} 입니다".format(a))

