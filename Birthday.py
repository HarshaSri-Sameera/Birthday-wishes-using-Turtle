import turtle
import random

def draw_background():
    turtle.penup()
    turtle.goto(-400, 300) 
    turtle.pendown()
    turtle.fillcolor("lightblue")  
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(800)  
        turtle.right(90)
        turtle.forward(600)  
        turtle.right(90)
    turtle.end_fill()

    turtle.color("yellow")
    for _ in range(20):  
        x = random.randint(-380, 380)
        y = random.randint(-280, 280)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        for _ in range(5):  
            turtle.forward(10)
            turtle.right(144)  
        turtle.end_fill()

def draw_cake():
    turtle.penup()
    turtle.goto(-70, -100)  
    turtle.pendown()
    turtle.fillcolor("pink")  
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(140)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-50, -50)  
    turtle.pendown()
    turtle.fillcolor("lightpink") 
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)
    turtle.end_fill()

    candle_positions = [-30, 0, 30]
    for candle_x in candle_positions:
        turtle.penup()
        turtle.goto(candle_x, 0)  
        turtle.pendown()
        turtle.fillcolor("red") 
        turtle.begin_fill()
        turtle.goto(candle_x, 20)
        turtle.goto(candle_x + 5, 20)
        turtle.goto(candle_x + 5, 0)
        turtle.end_fill()

        
        turtle.penup()
        turtle.goto(candle_x + 2.5, 20)  
        turtle.pendown()
        turtle.fillcolor("yellow")  
        turtle.begin_fill()
        turtle.circle(3)  
        turtle.end_fill()

def draw_text():
    turtle.penup()
    turtle.goto(0, 50)  
    turtle.pendown()
    turtle.color("black")
    turtle.write("Happy Birthday <Name>!", align="center", font=("Roman", 24, "italic"))

def main():
    turtle.speed(3)
    draw_background()  
    draw_text()
    draw_cake()

    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
