import turtle
t = turtle.Turtle()
# t.shape("turtle")
def rond(x):
  for i in range(x):
    t.right(1)
    t.forward(1)

def inima():
  t.fillcolor("red")
  t.begin_fill()
  t.left(140)
  t.forward(112)
  rond()
  t.left(120)
  rond()
  t.forward(112)
  t.end_fill()
  
def buline(x,y,d):
  merge(x,y)
  t.dot(d)
  t.left(90)
  t.fd(d/3)
  t.left(90)
  t.fd(d/3)
  t.dot(d)


t.speed(300)

def merge(x,y):
  t.pu()
  t.goto(x,y)
  t.pd()
  
merge(-100,-200)
t.color("#003049")
t.pensize(5)
t.fillcolor("#003049")
t.begin_fill()
t.left(90)
t.fd(30)
t.circle(-30,90)
t.position()
t.fd(60)
t.circle(-30,70)
t.fd(70)
t.goto(-100,-200)
t.end_fill()
merge(-77, -140)
t.setheading(90) # aici incepe capul

t.color("#fcbf49")
t.fillcolor("#fcbf49")
t.begin_fill()
t.fd(100)
t.position()
t.circle(-50,180)
t.position()
t.fd(35)
t.right(90)
t.fd(30)
t.left(90)
t.position() # incepe guritza
t.circle(20,90)
t.fd(10)
t.right(90)
t.fd(12)
t.circle(-13,90)
t.fd(10)
t.left(90)
t.fd(20)
t.end_fill()

merge(23,-40)
t.pensize(3)
t.right(16)
t.color("#f77f00")
t.fillcolor("#f77f00")
t.begin_fill()
t.fd(25)
t.setheading(0)
t.fd(15)
t.left(110)
t.fd(25)
t.end_fill()
merge(7,-40)
t.color("white")
t.dot(12)
t.color("black")
t.dot(6)
t.color("#f77f00")
merge(-15,-70)
t.dot(40)
merge(-77.0, -65)
t.pensize(5)
t.setheading(0)



buline(0,0,50)
buline(-15,0,10)
buline(-20,-5,30)
buline(-5,-10,10)
buline(-30,-25,40)
buline(-40,-20,40)
buline(-20,-15,50)
buline(-55,-20,40)
buline(-40,-25,40)
buline(-50,-25,40)
buline(-60,-30,40)
buline(-55,-25,50)
buline(-65,-50,50)
buline(-66,-55,10)
buline(-64,-65,40)
buline(-40,-20,40)
buline(-20,-15,40)
buline(-55,-20,40)
buline(-67,-67,40)
buline(-50,0,40)

merge(-77, -140)
t.setheading(90)
t.color("#d62828")
t.fillcolor("#d62828")
t.begin_fill()
t.fd(10)
t.right(90)
t.fd(40)
t.right(15)
t.fd(40)
t.goto(-77, -140)
t.end_fill()

