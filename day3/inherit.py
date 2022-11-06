'''
class Animal :
    def move(self):
        print('움직이는 생물')

class Dog(Animal):
    def my(self):
        print('나는 개')

dog1 = Dog()
dog1.my()
dog1.move()

class Horse(Animal):
    pass
horse1 = Horse()
horse1.move()
'''
'''
class Person:
    def __init__(self,name, age, gender):
        # 인스턴스 변수
        self.name = name
        self.age = age
        self.gender = gender
    
    def show(self):
        print('{}님의 나이는 {}이고 성별은 {}입니다'.format(self.name,self.age,self.gender))

#부모 클래스 Person 의 속성과 메소드를 상속받는 자식 클래스
class Child(Person):
    def __init__(self,name,age,gender,addr,hp):
        # Person.__init__(self,name,age,gender)
        super().__init__(name,age,gender)
        self.addr = addr
        self.hp = hp
        
    def playgame(self):
        print('지금 {}는 게임중'.format(self.name))
        
    def show(self):
        print('{}님의 나이는 {}이고, 성별은 {}이고, 주소는 {}이고 전화번호는 {} 입니다'.format(self.name,self.age,self.gender,self.addr,self.hp))
        

class Son(Person):
    def __init__(self,name,age,gender,addr,hp):
        Person.__init__(self,name,age,gender)
    
    def sleep(self):
        print('지금 {} 는 자고 있는 중입니다.'.format(self.name))
        
#인스턴스 생성
chulsu = Child('배철수',26,'남','서울','010-8888-8888')
chulsu.show()
chulsu.playgame()

euijoo = Son('이의주',15,'남','보령','010-1234-1234')
euijoo.show()
euijoo.sleep()

# 상속 관계 확인 맨 오른쪽이 부모클래스, 왼쪽으로 갈수록 자식 클래스
print(Person.mro())
print(Son.mro())
print(Child.mro())
'''

'''
print('start')
class Parent:
    def printdata(self):
        pass
class Child1(Parent):
    def printdata(self):
        print('Child1에서 override')

class Child2(Parent):
    def printdata(self):
        print('Child2에서 overriding')
        print('부모 메소드와 이름은 같으나 기능은 다름')
c1 = Child1()
c1.printdata()
c2 = Child2()
c2.printdata()  

# 다형성 처리
par = c1
par.printdata()

par = c2
par.printdata()

plist = [c1,c2]
for item in plist:
    item.printdata()
'''
'''
#Calculator - class.py
# 부모 클래스 Calc : 인스턴스 변수 2개 , show()메서드 오버라이딩
# 자식 클래스 Add, Sub, Mul, Div -> 변수 2개를 상속 받아서 사칙연산 결과 출력 / 추가속성 (거듭제곱)

class Calc :
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
   
    def show(self):
        print('{},{}'.format(self.x,self.y))

class Child(Calc):
    def __init__(self,x,y):
        super().__init__(x,y)
    
    def add(self):
        result = self.x + self.y
        print(result)
    def sub(self):
        result = self.x - self.y
        print(result)
    def mul(self):
        result = self.x * self.y
        print(result)
    def div(self):
        result = self.x / self.y
        print(result)
        
    def show(self):
        print('끝')
        
        
        
hap = Child(1,2)
hap.add()
hap.show()
cha = Child(1,2)
cha.sub()
hap.show()
gop = Child(1,2)
gop.mul()
hap.show()
nanut = Child(1,2)
nanut.div()
hap.show()
'''

'''

class Phone:
    def __init__(self):
        self.msg_list = []
        
    def call(self,num):
        return num
    def read_msg(self,index):
        print(self.msg_list[index])
    def write_msg(self,msg):
        self.msg_list.append(msg)
        print(self.msg_list)
    def send_msg(self,msg):
        pass
    
        
p1 = Phone()
p2 = Phone()
p3 = Phone()

p1.write_msg('코로나')
p1.write_msg('싫음')
'''
# # 부모 클래스
# class Phone:
#     phone_name = '피쳐폰'
 
#     def __init__(self, my_number, my_name):
#         print('Phone 생성자 호출')
#         self.my_number = my_number
#         self.my_name = my_name
 
#     def call(self, number):
#         print(f'Phone 전화걸기 : {number}')
 
#     def send_msg(self, number, msg):
#         print(f'Phone 메시지 보내기 : {number}, {msg}')
 
#     def get_info(self):
#         print(f'Phone 내 번호 : {self.my_number}')
#         print(f'Phone 내 이름 : {self.my_name}')
 
 
# # 자식 클래스 1 : 사과폰
# class ApplePhone(Phone):
#     def __init__(self, my_number, my_name,):
#         super(ApplePhone, self).__init__(my_number, my_name)  # 부모 클래스 생성자 호출
#         print('ApplePhone 생성자 호출')
 
#     def button_home(self):
#         print('ApplePhone 홈 버튼 눌림')
 
 
# # 자식 클래스 2 : 우주폰
# class GalaxyPhone(Phone):
#     def __init__(self, my_number, my_name):
#         super(GalaxyPhone, self).__init__(my_number, my_name)  # 부모 클래스 생성자 호출
#         print('GalaxyPhone 생성자 호출')
 
#     def button_cancel(self):
#         print('GalaxyPhone 취소(뒤로가기) 버튼이 눌렸습니다')
 
 
# # 클래스 생성
# print('\n1. 각 클래스의 객체 생성')
# phone = Phone('010-2222-2222', '폰은정')
# apple = ApplePhone('010-1234-5678', '김멸치')
# galaxy = GalaxyPhone('010-4321-4321', '김근육')
 
# # 부모 클래스로 부터 물려받은 메서드
# print('\n2. 부모 클래스의 메서드 호출')
# phone.get_info()
# apple.get_info()
# galaxy.get_info()
# apple.call('010-0000-0000')
# apple.send_msg('010-0000-1234','안녕')
# galaxy.call('010-1234-124')
# galaxy.send_msg('010-1234-1234','hi')
 
# # 본인 메서드
# print('\n3. 자식 클래스의 메서드 호출')
# apple.button_home()
# galaxy.button_cancel()