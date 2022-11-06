# class Car:
#     	def __init__(self):
#             print('자동차 불림')
    
# car = Car()

'''
class BananaPhone:
    phone_name = '어른폰'
 
    def __init__(self, number, owner):
        self.number = number
        self.owner = owner
 
    def print(self):
        s = f'이 폰은 {self.phone_name} 기종이며\n'
        s += f'번호는 {self.number} 이고\n'
        s += f'이 폰의 주인은 {self.owner} 입니다.\n'
        print(s)
 
 
# 객체, 인스턴스 생성
p1 = BananaPhone('010-1111-2222', '개님')
p2 = BananaPhone('010-7777-0000', '고양이님')
 
p1.print()
p2.print()
'''

'''
#클래스 예제
#게임 캐릭터 클래스 
#속성 : name(이름), score(점수), power(공격력)  
#동작 : __init__
    # live : 점수가 0이면 die, 점수가 0이상이면 alive    -> def로 선언
    # damage : 캐릭터의 점수가 0보다 큰 상태에서 파라미터로 power 전달 받아서 점수 - power 계산
    # __str__ : 계산 결과를 문자열로 출력해 주는 메서드
# ch1, ch2


class Ch:
    name = ''
    score = 0
    power = 0
    
    def __init__(self,name,score,power):
        self.name = name
        self.score = score
        self.power = power
    
    def live(self):
        statement = ''
        if self.score >0 :
            statement = True
        else :
            statement = False
        return statement
    # 캐릭터가 살아 있으면 공격 캐릭터의 공격력 만큼 체력 감소
    # 이미 캐릭터가 죽었으면 죽었다는 메시지 출력
    # 남은 체력보다 공격력이 더 크면 체력은 0
    
    def damage(self,attack):
       if self.live():
           self.score = self.score - attack     
       else:
           print('{}는 이미 die'.format(self.name))
    
    def other(self,other_ch):
        #캐릭터가 살아 있으면 다른 캐릭터의 체력을 자신의 공격력 만큼 감소
        if self.live():
            other_ch.damage(self.power)
    
    def __str__(self) :
        return '{}님의 score는 {}, 공격력은 {}입니다'.format(self.name,self.score,self.power)
    
    
#인스턴스 생성
ch1= Ch('이의주',100,100)
ch2= Ch('홍길동',200,50)

print(ch1)
print(ch2)

ch2.other(ch1)
print(ch2)
'''

'''
#클래스 예제 (주문받기)
# 1. 비빔밥 7000
# 2. 짜장면 8000
# 3. 잔치국수 3000
# 4. 돈가스 7500
# 5. 순대국 8500

# 메뉴를 선택하세요 : (키보드로 번호 입력받음)
# 4 돈가스 7500
# 계속 주문하려면 메뉴 번호를, 계산하려면 0을 누르세요 (키보드로 입력받음)


class Menu :
    
    def __init__(self):
        self.menu = ['','비빔밥','짜장면','잔치국수','돈가스','순대국']
        self.price = [0,7000,8000,3000,7500,8500]
        self.bill = [0,10000,8000,5000]
        self.total = 0
        
    def print_menu(self):
        for i in range(1,6):
            print(i,self.menu[i],self.price[i])
    
    def input_num(self):
        
        num = int(input('메뉴번호를 입력해주세요'))
        print(num,self.menu[num],self.price[num])
        self.total = self.total + self.price[num]
        
        #input menu == choicMenu
            
        while num != 0:
            num = int(input('계속 주문하려면 메뉴 번호를, 계산하려면 0을 누르세요'))
            if num >0 and num < len(self.menu):
                print(num,self.menu[num],self.price[num])
                self.total = self.total + self.price[num]
                
            else :
                print('주문 완료!.')
            
            
        return num
    
    def payment(self):
        pay = 0
        for i in range(1,4):
            print(i, self.bill[i],end = '')
            
        print()
            
        num = int(input('지불할 금액을 입력하세요'))
        if num >0 and num <len(self.bill):
            pay = pay + self.bill[num] - self.total
            
            if pay<0 :
                print('총 지불액은 %d 입니다',(-1)*pay) 
            else :
                print('거스름돈은 %d 입니다',pay)
                
            
            
        else:
            print('다시 선택해주세요')

num = 0
while num != 999:
    menu1 = Menu()
    menu1.print_menu()
    menu1.input_num()
    menu1.payment()
    num = int(input('주문 끝내려면 999, 다시 주문하려면 1을 누르세요'))
    


    

# 주문 완료!
# 1. 10000, 2. 8000, 3. 5000
# 지불할 금액을 입력하세요 : (키보드로 숫자 입력받음)

# 지불 금액 : 10000
# 거스름돈 : 2500
# 주문 끝내려면 999, 다시 주문 하려면 1을 누르세요(키보드 입력)

# 인스턴스 생성
'''