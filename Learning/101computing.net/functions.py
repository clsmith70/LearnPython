#A procedure to draw a circle of a given colour and size
import turtle
pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(500)
pen.hideturtle()

def drawCircle(x, y, color, size):
  pen.penup()
  pen.goto(x,y)
  pen.pendown()
  pen.color(color)
  pen.fillcolor(color)
  pen.begin_fill()
  pen.circle(size)
  pen.end_fill()
  
def drawStar(x, y, color, size):
  pen.penup()
  pen.goto(x,y)
  pen.pendown()
  pen.color(color)
  pen.fillcolor(color)
  pen.begin_fill()
  for i in range(5):
    pen.right(144)
    pen.forward(size)
  pen.end_fill()

def addText(x,y,text,color,size):  
  pen.penup()
  pen.goto(x,y)
  pen.pendown()
  pen.color(color)
  pen.write(text, None, align="center",font=("Arial", size, "normal"))