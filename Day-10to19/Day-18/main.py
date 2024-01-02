from turtle import Turtle, Screen,colormode
import random

# import turtle as t 
# tim = t.Turtle()
colormode(255)

tim = Turtle()
screen = Screen()

# tim.shape("turtle")
# tim.color("goldenrod4") #https://cs111.wellesley.edu/reference/colors

# def square():
#     for _ in range(4):
#         tim.forward(100)
#         tim.rt(90)

# square()

# import heroes
# print(heroes.gen())

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# def draw_shape(no_of_sides):
#     angle = 360/no_of_sides
#     # R = random.random()
#     # B = random.random()
#     # G = random.random()
#     # tim.color(R,G,B)
#     tim.color(random.choice(colours))
#     for _ in range(no_of_sides):
#         tim.forward(100)
#         tim.rt(angle)

# for sides in range(3,11) :
#     draw_shape(sides)

def random_color():
    R = random.randint(0,255)
    B = random.randint(0,255)
    G = random.randint(0,255)
    return (R,B,G)

# tim.width(15)
# tim.speed("fastest")

# def random_walk():
#     angle_list = [0,90,180,270]
#     for _ in range(200):
#         tim.color(random_color())
#         tim.forward(30)
#         tim.setheading(random.choice(angle_list))


# random_walk()

def spirograph():
    tim.speed(0)
    for direction in range(0,360,5):
        tim.setheading(direction)
        tim.color(random_color())
        tim.circle(100)

spirograph()
screen.exitonclick()
