import colorgram
import turtle as t
import random

t.colormode(255)

# Uses colorgram module to extract a specified number of colors from an image
# saved to project called 'spot_image.jpg'
colors = colorgram.extract('spot_image.jpg', 15)
color_list = [(220, 149, 107), (140, 119, 8), (73, 127, 125), (14, 122, 175), (56, 10, 10), (78, 40, 65), (185, 90, 156), (56, 165, 55), (226, 152, 223), (119, 8, 14), (4, 86, 120), (251, 251, 0)]

tim = t.Turtle()
screen = t.Screen()
tim.speed("fastest")


# This code is run initially to extract a list of RGB colors present in an image.
## Then manually removed the white and very close to white (with close to 255 values)
## from color_list
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_list.append(new_color)

# print(color_list)
dot_count = 100
row_count = int(dot_count / 10)

def draw_row():
    for n in range(row_count):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.setheading(0)

tim.hideturtle()
tim.setheading(225)
tim.penup()
tim.forward(350)
tim.setheading(0)

for r in range(row_count):  # Number of rows
    draw_row()




screen.exitonclick()