#-*- coding=utf-8 -*-

class Count():
    def plus(self,a,b):
        x=int(a)
        y=int(b)
        return x + y

    def minus(self,a,b):
        x=int(a)
        y=int(b)
        return x - y

if __name__=="__main__":
    c =  Count()
    a = c.minus(5,8)
    print(a)