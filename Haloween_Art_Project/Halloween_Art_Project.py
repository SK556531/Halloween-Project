# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
import turtle as trtl2
import turtle as trtl3
import turtle as trtl4
import turtle as trtl5

#-----game configuration----
cone_candy = trtl.Turtle()
score_writer = trtl2.Turtle()
counter = trtl3.Turtle()
ghost = trtl4.Turtle()
cone_candy2 = trtl5.Turtle()
spot_shape="circle"
spot_color="green"
spot_fillcolor="green"
spot_size=2
spot_speed=0
score=0
score_writer_color="green"
counter_color="red"
start_font=("Arial",100,"normal")
new_xpos=0
new_ypos=0
wn = trtl.Screen()
#-----countdown variables-----
font_setup = ("Arial", 20, "normal")
timer = 60
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----initialize turtle-----
cone_candy.shape(spot_shape)
cone_candy.color(spot_color)
cone_candy.fillcolor(spot_fillcolor)
cone_candy.shapesize(spot_size)
cone_candy.speed(spot_speed)
cone_candy2.shape(spot_shape)
cone_candy2.color(spot_color)
cone_candy2.fillcolor(spot_fillcolor)
cone_candy2.shapesize(spot_size)
cone_candy2.speed(spot_speed)
score_writer.color(score_writer_color)
counter.color(counter_color)
#Image


wn.addshape('animated-candy.gif')
cone_candy.shape('animated-candy.gif')

wn.addshape('giphy.gif')
wn.bgpic('giphy.gif')

wn.addshape('04361e7ffcbddcf90d543aee17f67d64_w200.gif')
ghost.shape('04361e7ffcbddcf90d543aee17f67d64_w200.gif')

wn.addshape('candy_2(2).gif')
cone_candy2.shape('candy_2(2).gif')

#-----game functions--------
def spot_clicked(x,y):
  if (timer_up!=True):
    ghost.goto(cone_candy.xcor(),cone_candy.ycor())
    ghost.clear()
    update_score()
    if(score==10):
      cone_candy2.showturtle()
      change_position_2()
    change_position()

  else:
    cone_candy.hideturtle()

def spot_clicked_2(x,y):
  if (timer_up!=True):
    ghost.goto(cone_candy2.xcor(),cone_candy2.ycor())
    ghost.clear()
    update_score()
    change_position_2()
  else:
    cone_candy2.hideturtle()

def change_position():
  new_xpos=rand.randint(-400,400)
  new_ypos=rand.randint(-300,300)
  cone_candy.penup()
  cone_candy.hideturtle()
  cone_candy.goto(new_xpos,new_ypos)
  cone_candy.pendown()
  cone_candy.showturtle()

def change_position_2():
  new_xpos=rand.randint(-400,400)
  new_ypos=rand.randint(-300,300)
  cone_candy2.penup()
  cone_candy2.hideturtle()
  cone_candy2.goto(new_xpos,new_ypos)
  cone_candy2.pendown()
  cone_candy2.showturtle()
def update_score():
  global score
  score+=1
  if (score != 1):
    score_writer.clear()
  score_writer.write(score, font=font_setup)
def draw_box():
  cone_candy.pendown()
  for t in range(2):
    cone_candy.forward(125)
    cone_candy.lt(90)
    cone_candy.forward(45)
    cone_candy.lt(90)

def update_score_2():
  global score
  score-=1
  if (score != 1):
    score_writer.clear()
  score_writer.write(score, font=font_setup)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

#-----events----------------
cone_candy2.penup()
cone_candy2.hideturtle()
cone_candy2.goto(400,400)
cone_candy.hideturtle()
cone_candy.penup()
cone_candy.goto(320,350)
draw_box()
cone_candy.penup()
cone_candy.goto(175,350)
draw_box()
cone_candy.penup()
cone_candy.goto(0,0)


score_writer.penup()
score_writer.goto(330,350)

counter.penup()
counter.goto(180,350)
cone_candy.showturtle()


change_position()

cone_candy.onclick(spot_clicked)
cone_candy2.onclick(spot_clicked_2)




wn.bgcolor("black")
wn.ontimer(countdown, counter_interval)
wn.mainloop()