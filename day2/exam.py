## 클라우드 엔지니어 과정 이의주

# #1번 1~100사이의 정수 중에서 3의 배수의 합을 출력하시오 while문을 쓸 것.

# i = 1
# sum =0
# while i<=100:
#     i +=1
#     if i%3==0:
#         sum = sum + i
# print(sum)




# #2번 1~100사이의 정수 중에서 3의 배수이나 2의 배수가 아닌 수를 출력하고, 합을 구하여 출력하시오 while문으로 구현 할 것.

# i = 1
# sum=0
# while i<=100:
#     i+=1
#     if ((i%3==0) and (i%2!=0)):
#         sum = sum + i
#         print(i)
# print(sum)




# #3번 정수 -1,3,-5,7,-9 ...~99 까지의 합을 출력하시오 while문으로 구현 할 것.

# i = -3
# sum1 = 0
# while i<=94:
#     i = i + 4
#     sum1 = sum1 +i

# j=-1
# sum2 = 0
# while j<=95:
#     j = j+4
#     sum2 = sum2 + j

# print((-1)*sum1 + sum2)



# #4번 별모양 쌓기
# i=0
# while i<5:
#     i+=1
#     print("*"*i)



# #5번 중첩 while문을 사용하여 구구단 중에서 2단, 3단을 출력하시오.
# i=2
# while i<4:
#     j=1
#     while j<10:
#         print('{} * {} = {}'.format(i,j,i*j))
#         j+=1
#     i+=1



# #6번 while문과 break 문을 사용하여 컴퓨터의 1~10사이의 랜덤한 수와 사용자가 입력한 정수를 맞추는 프로그램 구현

# import random
# num = random.randint(1,10)

# while True:
#     i = int(input('1~10사이 정수 입력해주세요'))        
#     if num==i:
#         print('정답 컴퓨터 :{},당신{}'.format(num,i))
#         break



# #7번 직원자료 문제

# import time
# from unicodedata import name
# now = time.localtime()
# today = int(now.tm_year)

# geunsok = 0
# gongjae = 0

# id = str(input('id?'))
# name = str(input('name?'))
# standard = int(input('standard?'))
# year = int(input('year?'))


# #근속수당 계산

# if (today - year -1) >=0 and (today - year -1)<=3 :
#     geunsok == 500000
# elif (today - year -1) >=4 and (today - year -1)<=8 :
#     geunsok == 1000000
# else :
#     geunsok == 1500000
    
# #공제액 계산

# if (standard + geunsok) >= 5000000 :
#     gongjae = (standard + geunsok) * 0.03
# elif (standard + geunsok) >= 4000000 :
#     gongjae = (standard + geunsok) * 0.02
# else :
#     gongjae = (standard + geunsok) * 0.01




# print('사번 이름 기본급 근무년수 근속수당 공제액 수령액')
# print('{} {} {} {} {} {} {}'.format(id,name,standard,today-year,geunsok,gongjae,standard + geunsok - gongjae))


# while True:
#     choice = str(input('계속하시겠습니까?[y/n]'))
#     if choice == 'y':
#         id = str(input('id?'))
#         name = str(input('name?'))
#         standard = int(input('standard?'))
#         year = int(input('year?'))
#     else:
#         break
    
# # 어렵습니다...!! 일단 나중에 도전



# #7 번 시작
# from http.client import PAYMENT_REQUIRED
# import time
# from unittest import result

# yn = 'y' #데이터를 더 입력받을 거면 True, 끝날거면 False
# count = 0 #데이터 입력 받은 건수
# result = ''

# now= time.localtime() #현재 시스템의 날짜와 시간
# #print(now)
# today = int(now.tm_year) #현재 날짜에서 년도만 뽑아서 today에 저장
# #print(today)

# #사원의 정보 입력받기
# while yn=='y':
#     data = input('사번, 이름, 기본급, 입사년도 입력하세요 :')
#     # print(data)
#     # data의 내용을 쉼표를 기준으로 분리시킴
#     list = data.split(',')
#     # print(list[1])
#     no = list[0] #사번
#     name = list[1] #이름
#     pay = int(list[2]) #기본급
#     year = int(list[3]) #입사년도
#     year2 = today - year #근무년수
    
#     if year2 >=9:
#         pay2 = 1500000
#     elif  year2 >=4:
#         pay2 = 1000000
#     else:
#         pay2 = 500000 #수당표에 의한 근속 수당 계산
        
    
#     totalpay = pay + pay2  #급여액
    
#     #공제액 계산
#     if totalpay >= 5000000:
#         tax = totalpay * 0.03
#     if totalpay >= 4000000:
#         tax = totalpay * 0.02
#     else:
#         tax = totalpay * 0.01
#     # 실수령액
#     realpay = totalpay - tax
#     # 처리건수 증가
#     count +=1
#     #출력 
#     result+= '%s\t%s\t%d\t%d\t%d\t%d\t%d\n'%(no, name, pay, year2, pay2, tax, realpay)
    
#     yn = input('계속 입력하시겠습니까? [y/n]')

# print('사번\t이름\t기본급\t 근무년수\t 근속수당\t 공제액\t 수령액\n')
# print(result)
# print('처리 건수 : %d'%count)












# #8번 두개의 리스트 각요소의 차이 계산하기

# panmaeSudang = [55,67,100]
# insaSudang = [50,60,100]

# i = 0
# diff = []

# for i in range(3):
#     diff = panmaeSudang[i] - insaSudang[i]
#     print(diff)



# #9번 1~100 사이의 정수 중 3의 배수 이고 5의 배수인 정수의 합 for문으로 구현

# sum = 0
# for i in range(100):
#     i +=1
#     if i%3==0 and i%5==0:
#         print(i)
#         sum = sum + i
# print(sum)




# #10번 for문 사용하여 구구단을 완성하기

# for i in range(2,10):
#     for j in range(1,10):
#         print('{} * {} = {}'.format(i,j,i*j),end = '\t')
#         if j==9 :
#             print()