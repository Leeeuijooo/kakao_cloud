# #사용자 정의 함수
# def fn(): #매개변수 없는 함수
#     print('***')

# def addfn(a,b):
#     res = a + b
#     return res
# #함수 호출
# fn() #매개 변수 없는 함수 호출
# print(addfn(10,20))
# print(addfn(25.6, 50.9))

# def addfn(x,y):
#     res = x + y
#     return res

# def subfn(x,y):
#     res = x - y
#     return res

# def multifn(x,y):
#     res = x * y
#     return res

# def divfn(x,y):
#     res = x / y
#     return res

# print(divfn(10,5))

# def isodd(arg):
#     return arg % 2 == 1
# res = {x : x*2 for x in range(1,11) if isodd(x)} #홀수 이면!
# print(type(res))
# print(res)

# player = '전국대표'

# def fun():
#     name = '홍길동'
#     player = '지역대표'
#     print(name, player)
    
# fun()

# 가변 인수 처리

# # 람다 함수
# print((lambda x,y:x+y)(10,20))

#map(함수 , 리스트)

# from functools import reduce


# res = list(map(lambda x:x**2,range(10)))
# print(res)
#reduce(함수, 시퀀스)
# res2 = reduce(lambda x,y : x+y , [0,1,2,3,4,5])
# print(res2)

# # filter(함수,리스트)
# res3 = list(filter(lambda x:x<5, range(10)))
# print(res3)

#재귀함수
def tot(n):
    print(n)
    if n==1:
        print("탈출")
        return True
    return n+tot(n-1)

rs = tot(10)
print(rs)
# # 연습문제 1
# datas = [1,3,5,7,9,2,4,6]
# def checkfunc(datas,x):
#     for i in datas:
#         if i == x:
#             print('있어요')
#         else:
#             print('없어요')

# checkfunc(datas,8)

# from unittest import result


# yn = 'y'
# count = 0
# sum = 0

# def inputfunc():
#     while yn == 'y':
#         data = input('지역코드, 상품명, 수량 입력하세여 :')
#         list = data.split(',')
        
#         no = list[0]
#         product = list[1]
#         n = int(list[2])
        
#         if no == 100:
#             region = '강북'
#         else:
#             region = '강남'
            
        
#         if product == '새우깡':
#             dan = 450
            
#         else:
#             dan = 300
            
#         pay = dan * n
#         count +=1
#         sum = sum + pay
        
#         result += '%s\t%s\t%d\t%d\t%d\n'%(region,product,n,dan,pay)
#         yn = input('계속 입력하시겠습니까? [y/n]')
        
# inputfunc()
# # 다시 해볼것
