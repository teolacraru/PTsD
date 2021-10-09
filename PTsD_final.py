import turtle
t = turtle.Turtle()

screen = turtle.Screen()
screen.bgcolor("#eae2b7") # culoarea fundalului

t.speed(100)

def mergexy(x,y): # se deplaseaza cu x pixeli pe Ox si y pe Oy
  t.pu()
  t.setheading(0)
  t.fd(x)
  t.setheading(90)
  t.fd(y)
  t.pd()
  
def merge(x,y): # se deplazseaza la pozitia (x,y)
  t.pu()
  t.goto(x,y)
  t.pd()
  
def mergex(x): # se deplaseaza pe axa Ox
  t.pu()
  t.setheading(0)
  t.fd(x)
  t.pd()
  
def mergey(y): # se deplaseaza pe axa Oy
  t.pu()
  t.setheading(90)
  t.fd(y)
  t.pd()
  
def virus(m,c,o): # functie pt virus
  t.color(c)
  unghi=0
  t.pensize(m/8)
  for i in range(15):
    t.fd(m)
    t.dot(m/4)
    t.bk(m)
    t.right(unghi+24)
  t.dot(2*m+m/2)
  t.color(o)
  mergex(m/3)
  t.dot(m/3+m/5)
  t.color("black")
  t.dot(m/3+m/5-m/6)
  mergex(-2*m/3)
  t.color("white")
  t.dot(m/3+m/5)
  t.color("black")
  t.dot(m/3+m/5-m/6)
  
  
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
t.setheading(90) # de aici incepe capul

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
t.position() # incepe gura
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
t.color("#f77f00") #culoarea nasului si a obrazului
t.fillcolor("#f77f00")
t.begin_fill()
t.fd(25)
t.setheading(0)
t.fd(15)
t.left(110)
t.fd(25)
t.end_fill()
merge(7,-40)

t.color("white") #ochiul
t.dot(12)
merge(9,-42)
t.color("black")
t.dot(6)
t.color("#f77f00")
merge(-15,-70)
t.dot(40)
merge(-77.0, -65)
t.pensize(5)
t.setheading(0)

t.pencolor("#e75414")
t.setheading(110)
merge(-75,-40)
t.dot(50)
for i in range(6): # pentru par
  u=0
  t.right(u+25)
  t.fd(20)
  t.dot(60)
t.setheading(180)
for i in range(5): # pentru par
  u=0
  t.right(u-10)
  t.fd(20)
  t.dot(50)

merge(-77, -140)
t.setheading(90)
t.color("#d62828") # pt guler
t.fillcolor("#d62828")
t.begin_fill()
t.fd(10)
t.right(90)
t.fd(40)
t.right(15)
t.fd(40)
t.goto(-77, -140)
t.end_fill()

merge(60, -200)
t.color("#D62828") # incepe corpul fetei
t.fillcolor("#D62828")
t.begin_fill()
t.setheading(90)
t.right(15)
t.fd(20)
t.circle(-20, 75)
t.position()
t.fd(35)
t.position()
t.circle(-20,90)
t.fd(20)
t.end_fill()

merge(123, -165)
t.color("#F3D180")
t.fillcolor("#F3D180") # capul fetei
t.begin_fill()
t.setheading(90)
t.fd(60)
t.circle(25,180)
t.position()
t.fd(23)
t.left(90)
t.fd(18)
t.left(90)
t.position()
t.circle(10,-80)
t.left(180)
t.fd(10)
t.left(80)
t.fd(3)
t.circle(8,90)
t.fd(5)
t.left(-90)
t.fd(12)
t.end_fill()

merge(73.0, -105.0)
t.pensize(1)
t.right(10)
t.color("#FBAF37")
t.fillcolor("#FBAF37") # nasul fetei
t.begin_fill()
t.fd(18)
t.setheading(0)
t.fd(10)
t.left(110)
t.fd(18)
t.end_fill()

merge(91, -128) # obrazul fetei
t.dot(16)

merge(85,-105)
t.color("white") # ochiul fetei
t.dot(9)
merge(84,-104)
t.color("black")
t.dot(5)

merge(73,-96)
t.setheading(0)
t.color("#003049")
t.fillcolor("#003049") # parul fetei
t.begin_fill()
t.fd(30)
t.right(90)
t.fd(60)
t.left(90)
t.fd(35)
t.setheading(180)
t.circle(-8,90)
t.fd(47)
t.circle(30,175)
t.end_fill()

merge(123, -165)
t.color("#6B2C39")
t.fillcolor("#6B2C39") # gulerul fetei
t.begin_fill()
t.setheading(-180)
t.pensize(6)
t.fd(38)
t.end_fill()

t.pencolor("white")
merge(70,20)
t.fillcolor("white")
t.begin_fill()
for i in range(10): # desenam norisorul
  ungh=0
  t.dot(40)
  t.left(ungh+36)
  t.fd(20)
t.end_fill()

t.pensize(2)
mergexy(-30, -100)
t.pencolor("white")
t.fillcolor("white")
t.begin_fill()
t.right(20)
t.fd(45)
t.right(90)
t.fd(20)
t.right(115)
t.fd(50)
t.end_fill()

merge(70,-17)
virus(20, "#1aa120", "white") # virusul din norisor

mergexy(40,25)
t.pensize(8)
t.color("red")
t.setheading(270) # semnul "!"
t.fd(25)
mergey(-10)
t.dot(9)

# virusi din fundal

merge(120, 120)
virus(60, "#51c257", "white")

merge(-190,-180)
virus(50, "#51c257", "white")

merge(-120, 130)
virus(40, "#51c257", "white")

merge(-150,10)
virus(30, "#51c257", "white")

merge(10, 60)
virus(20, "#51c257", "white")

merge(900,900)