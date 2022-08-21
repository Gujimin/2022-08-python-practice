a_tuple = ('안녕하세요','저는','박형준입니다.')
#CRUD : CREATE,REGIST,UPDATE,DELETE

#Deep copy 깊은 복사 = 메모리 주소를 복사 =b_list = a_list
#shallow copy 얉은 복사 = 값 복사 = .copy()
print(type(a_tuple))
a = list(a_tuple)
print(a)

#set == {} 리스트와 달리 순서가 없고 인덱싱이라는 개념이 없다
set_sample ={1,2,3,4,4,5} #중복이여도 하나만 출력
print(set_sample)

for i in set_sample:
    print(i)

dict_example = {
    '이름': '구지민',
    '성별': '남자',
    '나이': 20
}
print(dict_example.keys())
print(dict_example.values())