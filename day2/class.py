# #객체지향 프로그래밍 - 클래스

# class Human():
# #초기화 함수
#     def __init__(self,name,addr,gender):
#         self.name = name
#         self.addr = addr
#         self.gender = gender
        
#     def __str__(self):
#         return '{}님의 주소는{}이고, 성별은 {} 입니다.'.format(self.name,self.addr,self.gender)
    
# #인스턴스

# you = Human('유재석','서울','남')
# me = Human('이의주','서울','남')

# print(you)
# print(me)
# # you.run()
# # me.run()

# # 연습문제 클래스 이름은 Food로 / 속성 - 음식이름, 가격, 선호도(5점 만점) / 동작 - 선호도가 4점이상->추천메뉴, 2점이상->일반메뉴, 2점 미만이면->제거대상

# class Food():
    
#     def __init__(self,name,price,star):
        
#         self.name = name
#         self.price = price
#         self.star = star
        
        
    

#     def __str__(self):
#         if self.star >=4:
#             return '{}은 추천메뉴'.format(self.name)
         
#         elif self.star >=2:
#             return '{}은 일반메뉴'.format(self.name)
        
#         else:
#             return '{}은 제거 대상'.format(self.name)

# you = Food('감자탕',10000,4)
# print(you)

# #클래스 생성 
# class Counter:
#     def __init__(self, limit):
#         self.limit=limit
#         self.value = 0 #이 클래스 안의 멤버 변수라서 self 붙여준거임.
        
        
#     def set(self,new_value): #인스턴스를 생성할 때 limit만 값을 받고, value는 0으로 초기화
#         self.value = new_value if new_value >= 0 and new_value < self.limit else 0
#         #자연수만 받고 limit값보다 작은 값을 받겠다.
        
#     def tick(self):
#         # value값을 1증가 시킴
#         self.value +=1
        
#         if self.value == self.limit :
#             self.value = 0
#             return True
#         return False
    
#     def __str__(self):
#         return str(self.value).zfill(5) 

# count1 = Counter(24)
# count2 = Counter(60)
# count3 = Counter(60)

# #0부터 5까지 세기

# for i in range(30):
#     count1.tick()
#     print(count1)

# #타이머 값을 0으로 세팅
# count1.set(0)
# print(count1)




# class Car():
#     handle = 0
#     speed = 0
#     #누구나 접근 하는 변수
    
#     def __init__(self,name,speed): #초기화
    
#         self.name = name
#         self.speed = speed
        
#     def showData(self):
#         km = 'killo meter'
#         msg = 'speed : ' + str(self.speed) + km
#         return msg
# #인스턴스 생성
# car1= Car('tom',10)
# print(car1.handle,car1.name,car1.speed)

# car1.color = 'black'
# print('car1.color:',car1.color)

# car2 = Car('james',20)
# print(car2.handle,car2.name,car2.speed)

# print(id(Car), id(car1), id(car2))
# print('car1',car1.showData())
# print('car2',car2.showData())
# car1.speed = 50
# print('car1',car1.showData())

# print('car1 speed : ', car1.speed)
# print('car2 speed : ', car2.speed)

# print(Car.handle)


#다른 예제

# class Singer:
#     title_song = '아리랑'
    
#     def sing(self):
#         msg = '노래는'
#         print(msg,self.title_song,'룰랄')

# boys = Singer()
# print('타이틀 송은',Singer.title_song)
# print('boys:')
# boys.sing()

# girls = Singer()
# print('girls:')
# girls.sing()

# girls.title_song = '댄싱퀸'
# girls.sing()
# girls.co = 'FM'
# print('소속사:',girls.co)

# print(Singer.title_song)
# Singer.title_song = '아름다운 강산' #전역변수 값 바꿈
# print('타이틀 송은',Singer.title_song)
# boys.sing()
# girls.sing()

