import turtle as trtl1
import turtle as trtl2
import random as rand
wn = trtl1.Screen()
wn.bgcolor('lightblue')

timer_up=True

t = trtl1.Turtle()
candy = trtl2.Turtle()
score=0

t.color('red')
t.penup()

speed = 1

def travel():
    t.forward(speed)
    wn.ontimer(travel, 10)


wn.onkey(lambda: t.setheading(90), 'Up')
wn.onkey(lambda: t.setheading(180), 'Left')
wn.onkey(lambda: t.setheading(0), 'Right')
wn.onkey(lambda: t.setheading(270), 'Down')





wn.listen()

travel()

wn.mainloop()