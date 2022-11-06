
class Doonkey:
    data = '당나귀 최고'
    
    def skill(self):
        print('당나귀 : 짐나르기')
        
class Horse:
    def skill(self):
        print('말 : 달리기')
    def hobby(self):
        print('말은 달리기가 취미')
        
class Mule1(Horse,Doonkey): #호출 순서 유의 skill 메서드가 중복되나 가장 이른 순서가 호출된다.
    pass

mu1= Mule1()
print(mu1.data)
mu1.skill()
mu1.hobby()

class Mule2(Horse,Doonkey):
    def play(self):
        print('노새 고유 메서드')
        
    def hobby(self):
        print('노새는 걷기를 즐김')
    def showhobby(self):
        self.hobby()
        super().hobby()
        
    def showdata(self):
        print(self.data)
        print(super().data)
        
mu2 = Mule2()
mu2.skill()
mu2.hobby()
mu2.play()
mu2.showhobby()
mu2.showdata()
