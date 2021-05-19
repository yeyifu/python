import turtle

'''
t = turtle.Pen()
for x in range(360):
    t.forward(x)
    t.left(59)
'''

'''
t = turtle.Pen()
t.width(4)
t.speed(0)
colors = ('red','green','yellow','black','blue')

for i in range(10):
    t.goto(0,-i*10)
    t.color(colors[i%len(colors)])
    t.pendown()
    t.circle(10+i*10)
    t.penup()
turtle.done()
'''

'''
#棋盘
t = turtle.Pen()
t.speed(0)
for i in range(20):
    t.penup()
    t.goto(0,i*10)
    t.pendown()
    t.goto(19*10,i*10)

    t.penup()
    t.goto(i*10,19*10)
    t.pendown()
    t.goto(i*10,0)
turtle.done()
'''

