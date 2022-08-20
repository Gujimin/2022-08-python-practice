홀수합 = 0
짝수합= 0
전체합= 0
for i in range(1,101):
    전체합 = 전체합+ i
    if i % 2 == 0:
        짝수합= 짝수합 + i
    else:
        홀수합 = 홀수합 + i

print(짝수합)
print(홀수합)
