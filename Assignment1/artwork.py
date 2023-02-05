#Réda Alidrissi-Omari
#261068776

import turtle
    
    
def body(t, color):
    """ (turtle, string) -> None
    t draws kirby's body, which is a circle, and fill it with color
    """
    
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(100)
    t.end_fill()

def hands(t,color):
    """ (turtle, string) -> None
    t draws both kirby's hands, which are both circles, positions
    them accordingly, and fills them with color
    """
    
    t.color(color)
    t.fillcolor(color)
    
    t.penup()
    t.forward(125)
    t.left(90)
    t.forward(130)
    t.pendown()
    
    t.begin_fill()
    t.circle(35)
    t.end_fill()
    
    
    t.penup()
    t.right(80)
    t.backward(220)
    t.pendown()
    
    t.begin_fill()
    t.circle(35)
    t.end_fill()

def feet (t, color):
    """ (turtle, string) -> None
    t draws both kirby's feet, which are both ellipses, positions
    them accordingly, and fills them with color that is in a
    slightly darker tone than the body's and the hands' color
    """
    
    if color == "pink":
        t.color("deep" + color)
        t.fillcolor("deep" +color)
    elif color == "yellow":
        t.color("orange")
        t.fillcolor("orange")    
    else:
        t.color("dark " + color)
        t.fillcolor("dark " + color)
    
    t.penup()
    t.forward(65)
    t.right(90)
    t.forward(90)
    t.pendown()
    
    t.begin_fill()
    t.left(170)
    for x in range(2):
        t.circle(60,90)
        t.circle(60//2,90)
    t.end_fill()
    
    t.penup()
    t.backward(30)
    t.right(90)
    t.forward(60)
    t.left(90)
    t.pendown()
    
    t.begin_fill()
    t.right(85)
    for x in range(2):
        t.circle(60,90)
        t.circle(60//2,90)

    t.end_fill()
    
def eyes(t):
    """ (turtle) -> None
    t draws kirby's eyes, which are two straight lines, 
    positions and spaces them to look to the right
    (towards the other kirby next to it)
    """
    
    t.color("black")
    t.pensize(6)
    
    t.penup()
    t.backward(50)
    t.right(90)
    t.backward(125)
    t.left(90)
    t.pendown()
    
    t.left(85)
    t.forward(50)
    t.backward(50)
    
    t.penup()
    t.right(90)
    t.forward(50)
    t.left(90)
    t.pendown()
    
    t.forward(50)
    
def mouth(t):
    """ (turtle) -> None
    t draws kirby's mouth, which is a quarter circle, 
    positions it to look like a smiling mouth
    """
    
    t.penup()

    t.left(180)
    t.forward(65)
    t.right(90)
    t.forward(68)
    t.right(90)
    t.pendown()
    
    t.right(135)
    t.circle(60,90)
    

def kirby(t, color, position_x, position_y):
    """ (turtle, string, num, num) -> None
    t draws kirby's whole shape using other functions, color
    determines the color palette it will have, position_x
    and position_y determine the initial position of kirby
    """
    
    t.penup()
    t.goto(position_x, position_y)
    t.pendown()
    t.pensize(4)
    
    body(t,color)
    hands(t,color)
    feet(t, color)
    eyes(t)
    mouth(t)
    
    t.pensize(4)
    t.penup()
    t.right(45)

def star(t, color, side_length):
    """ (turtle, string, num) -> None
    t draws a star with equal sides which are determined by
    side_length using a for loop, and fills the star with color
    """
    
    angle = 100 
    t.right(20)
    
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    
    for i in range(5):
        t.forward(side_length)
        t.right(angle)
        t.forward(side_length)
        t.right(72 - angle)
    
    t.left(20)
    t.end_fill()
    t.penup()

def triangle(t):
    """ (turtle) -> None
    t draws a triangle using a for loop, and fills it with
    the color "SlateBlue4"
    """
    
    t.fillcolor("SlateBlue4")
    t.begin_fill()
    for i in range(3):
        t.forward(320)
        t.left(120)
    t.end_fill()
    
def signature(t):
    """ (turtle) -> None
    t draws the letter "R" which is my first name
    """
    
    t.color("thistle")
    t.pensize(6)
    
    t.left(90)
    t.forward(60)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(25)
    t.backward(12)
    t.left(115)
    t.forward(40)
    
def my_artwork():
    """ () -> None
    This function draws two triangles at the bottom corners,
    draws 8 kirbys with different colors,draws 4 stars
    and the signature at the middle of the smallest star
    """
    
    my_turtle = turtle.Turtle()
    my_turtle.speed("fastest")
    
    my_turtle.penup()
    my_turtle.goto(-640,-530)
    my_turtle.pendown()
    triangle(my_turtle)
    
    my_turtle.penup()
    my_turtle.goto(312,-530)
    my_turtle.pendown()
    triangle(my_turtle)
    my_turtle.penup()
    
    kirby(my_turtle, "pink", -350,0)
    kirby(my_turtle, "yellow", -100,0)
    kirby(my_turtle, "cyan", 150,0)
    kirby(my_turtle, "red", 400,0)
    kirby(my_turtle, "sea green", 400,-210)
    kirby(my_turtle, "orange", 150,-210)
    kirby(my_turtle, "violet", -100,-210)
    kirby(my_turtle, "gray", -350,-210)
    
    my_turtle.penup()
    my_turtle.right(3)
    my_turtle.goto(90,450)
    my_turtle.pendown()
    star(my_turtle, "DarkOrchid4",100)
    
    my_turtle.penup()
    my_turtle.goto(75,430)
    my_turtle.pendown()
    star(my_turtle, "DarkOrchid3",80)
    
    my_turtle.penup()
    my_turtle.goto(60,410)
    my_turtle.pendown()
    star(my_turtle, "DarkOrchid2",60)
    
    my_turtle.penup()
    my_turtle.goto(45,390)
    my_turtle.pendown()
    star(my_turtle, "DarkOrchid1",40)
    
    my_turtle.penup()
    my_turtle.goto(7,322)
    my_turtle.pendown()
    signature(my_turtle)
    
    my_turtle.hideturtle()
