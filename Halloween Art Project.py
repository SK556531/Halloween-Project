#-----import statements-----
import random as rand
import turtle as trtl
t = trtl.Turtle()
wn = trtl.Screen()
#-----game configuration----
#Image
wn.addshape('corn_candy.gif')
t.shape('corn_candy.gif')
#User Clicks
def spot_clicked(x,y):
  print("spot was clicked")
t.onclick(spot_clicked)

#-----game functions--------
def change_position():
  new_xpos=rand.randint(-400,400)
  new_ypos=rand.randint(-300,300)
  t.penup()
  t.hideturtle()
  t.goto(new_xpos,new_ypos)
  t.pendown()
  t.showturtle()



wn.mainloop()