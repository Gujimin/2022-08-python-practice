phone = input('전화번호를 입력하세요>>>')
a = phone.index('-') + 1
b = phone.index('-',a)
c = phone[a:b]
print(c)