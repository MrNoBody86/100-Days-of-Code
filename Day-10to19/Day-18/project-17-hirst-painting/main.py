# import colorgram

# rgb_color = []
# colors = colorgram.extract("Day-18\project-17-hirst-painting\hirst_painting.jpg",300)

# for color in colors :
#     r = color.rgb.r 
#     g = color.rgb.g 
#     b = color.rgb.b 
#     rgb_color.append((r,g,b))
import turtle as t
import random

color_palate = [(232, 231, 228), (204, 155, 90), (116, 162, 196), (230, 243, 236), (159, 82, 50), (152, 63, 97), (63, 99, 146), (244, 228, 236), (167, 154, 50), (218, 229, 238), (60, 123, 86), (193, 133, 158), (127, 185, 161), (189, 90, 123), (131, 27, 47), (226, 203, 121), (200, 94, 71), (82, 156, 130), (78, 22, 54), (43, 53, 106), (143, 35, 29), (152, 210, 193), (95, 123, 175), (75, 154, 166), (35, 36, 78), (228, 166, 188), (25, 63, 42), (152, 209, 217), (82, 38, 29), (32, 84, 59), (170, 187, 220), (225, 175, 167), (82, 86, 26), (27, 80, 92), (226, 201, 19)]
t.colormode(255)

tim = t.Turtle()
screen = t.Screen()
tim.penup()
tim.setpos(-225,-225)

for dot in range(10):
    new_y_corr = -225+ 50*dot
    tim.setpos(-225 , new_y_corr)
    for _ in range(10):
        tim.dot(20,random.choice(color_palate))
        tim.fd(50)

tim.ht()
screen.exitonclick()