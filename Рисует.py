from turtle import*
import random 
pensize(10)
speed(0)

move=10
rotation=20
long=200

colors = ['red', 'green', 'yellow', 'purple', 'orange']

a=1 # 1-случайные разммеры. не 1 уже заданные размеры

c=True

   
def random_per():
    return int(random.randint(-800, 800))

def random_vtor():
    return int(random.randint(-50, 50))

def drawin():
 
    while c:
        if a==1:
            move=random_vtor()
            rotation=random_vtor()
            long=random_vtor()
        else:
            move=10
            rotation=20
            long=200
            
        pencolor(random.choice(colors))        
        x=random_per()
        y=random_per()
        
        for i in range(14): # первое яйцо
            forward(move)
            left(rotation)
        left(-10)
        
        forward(long) # длинна хуя 

        for i in range(4): # половина окружности залупы
            right(22.5)
            forward(move)

        # залупная палочка
        right(90)
        forward(20)
        backward(20)
        left(90)
            
        for i in range(4): # вторая половина окружности залупы
            forward(move)
            right(22.5)
         
        forward(long)# длинна хуя
            
        backward(5) # исправление бага с немного разной длинной, хуй пойми из за чего, самым топорным методом 
            
        for i in range(14): # второе яйцо
            forward(move)
            left(rotation)
        left(-10)

        
            
        pu()
        goto(x, y)
        pd()

        c!=False


drawin()

print ("Хотите случайные размеры ")
string=input("0-Нет 1-Да  :" )







