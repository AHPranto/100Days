# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import random
import turtle as turtle_module

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(250, 250, 245), (238, 248, 242), (252, 243, 249), (242, 245, 251), (151, 27, 57), (72, 100, 158), (212, 153, 67), (47, 126, 81), (147, 67, 118), (122, 149, 193), (185, 75, 52), (152, 165, 56), (211, 147, 177), (29, 31, 60), (241, 215, 50), (207, 79, 58), (38, 56, 116), (86, 25, 38), (64, 160, 97), (82, 26, 24), (236, 217, 11), (110, 107, 165), (133, 181, 137), (118, 36, 33), (183, 89, 122), (228, 165, 187), (228, 177, 167), (30, 92, 55), (182, 184, 214), (159, 209, 180)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
