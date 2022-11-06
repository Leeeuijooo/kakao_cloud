# python Private : __quan , Public : 무

class Pi:
    quan = 0
    
    def leftT(self,quan):
        self.quan = quan
        
        return '죄회전'
    
    def rightT(self,quan):
        self.quan = quan
        
        return '우회전'

class Car :
    show = '정지'
    
    def __init__(self,ownerName):
        self.ownerName = ownerName
        self.handle = Pi() #has a (포함관계)

    def turnH(self,q):
        if   q>0:
            self.show = self.handle.rightT
        elif q<0:
            self.show = self.handle.leftT
        else:
            self.show = '직진'
            
            
tom = Car('tom')
tom.turnH(10)
print(tom.ownerName + '의 회전량은 ' + tom.show + str(tom.handle.quan))
