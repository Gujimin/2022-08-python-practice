exam =[]
while True:
    score = int(input('점수입력>>>'))
    if score < 0:
        break
    else:
        exam.append(score)
a = sum(exam)/len(exam)
b = max(exam)
c = min(exam)
print('평균 = {}, 최대 = {}, 최소 = {}'.format(a,b,c))