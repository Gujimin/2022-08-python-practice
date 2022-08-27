a = input("사업자등록번호를 입력하세요>>>")

if len(a) !=12:
    print("올바른 형식이 아닙니다.")
else:
   if a[3]=='-' and a[6] == '-':
       if a.replace('-','').isdecimal():
           print("올바른 형식입니다")
       else:
           print("올바른 형식이 아닙니다.")
   else:
       print("올바른 형식이 아닙니다.")





