#1번
# 커피자판기 프로그램 : 클래스 포함관계 관련 문제 
# 처리조건
# 입력자료는 키보드를 이용
# 커피는 1잔에 200원
# 100원을 넣고 커피를 요구하면 요금 부족 메시지 출력
# 400원을 넣고 2잔을 요구하면 2잔을 출력
# 500원을 넣고 1잔을 요구하면 커피 1잔과 잔돈 300원을 돌려준다
# 교재 167페이지 포함관게 has a 참고

# 출력 예)
# 동전을 입력하세요 :400
# 몇 잔을 원하세여 :2
# 커피 2잔과 잔돈 0원

# class Coinin:
#     coin = 0
#     chage = 0
    
    
#     def calc(self,cupCount):
#         if self.coin < 200:
#             print('요금부족')
#         else:
#             change = self.coin - cupCount * 200
            
#         return change
    

    
# class Machine:
#     cupCount = 1
#     def __init__(self):
#         self.coinIn = Coinin()
    
#     def showData(self):
#         self.coinIn.coin  = int(input('동전입력:'))
#         self.cupCount = int(input('몇잔 필요하세요:'))
#         print(self.coinIn.calc(self.cupCount))


# lee = Machine()
                

# 2번
# 처리조건
# 그림과 같이 부모클래스 Pen에 대한 자식 클래스 세개를 만들고, Pencil 과 Ballpen 클래스는 writeLetter 를 오버라이드 하고 
# Fountainpen 클래스는 오버라이드 하지 않는다. 객체 생성 후 다형성을 사용해 결과를 출력한다

# Pen 클래스의 writeLetter 메서드의 내용은 다음과 같다.
#         def writeLetter(self):
#             print('글씨를 쓴다')

class Pen:
    def __init__(self):
        pass
    def writeLetter(self):
        print('글씨를 쓴다')


class Pencil(Pen):
 
    def writeLetter(self):
        print('연필이 최고')
   

class Ballpen(Pen):

    def writeLetter(self):
        print('볼펜이 최고')


class Fountainpen(Pen):
    pass
    
pencil = Pencil()
ballpen = Ballpen()
fountainpen = Fountainpen()

pencil.writeLetter()
ballpen.writeLetter()
fountainpen.writeLetter()
