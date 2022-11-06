'''
from turtle import *
import _tkinter

class Ourturtle:
    def __init__(self):
        self.tt = Turtle()
        
    
    def shape(self,x):
        self.tt.shape(x)

class Car(Ourturtle):
    def go(self,x):
        for i in range(x):
            self.tt.left(90)
        self.tt.foward(100)
        for i in range(4-x):
            self.tt.left(90)
    
    def move(self,x):
        if x ==up:
            self.go(1)
        elif x==down:
            self.go(3)
        elif x==right:
            self.go(4)
        else:
            self.go(2)

#인스턴스 생성
t= Car()
p= Car()

t.shape('turtle')
p.shape('circle')

t.move(right)
t.move(down)
t.move(right)

p.move(left)
p.move(up)
p.move(left)
'''