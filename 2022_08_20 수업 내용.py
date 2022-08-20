#리스트와 튜플
a_list = [1,2,3,4,5]  # list ==[] :변경 가능
print(a_list)

a_tuple =(1,2,3,4,5) # tuple == () :변경 불가
a_list.append('추가')
print(a_list)

sum = 0
for i in range(1,100):
    sum = sum + i
print(sum)


a_list.insert(1,'첫번')
print(a_list)
a_list.remove('첫번')
print(a_list)
a_list.pop()
print(a_list)


b_list = a_list.copy()
print(b_list)
#조건문
print("성인입니다")