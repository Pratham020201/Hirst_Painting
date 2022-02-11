#CODE FOR EXTRACTING COLOURS FROM THE IMAGE:
# import colorgram
# color_list = []
# colors = colorgram.extract('image.jpg', 35)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new = (r, g, b)
#     color_list.append(new)
# print(color_list)
#COLOR LIST OBTAINED:
import turtle

color_list= [ (198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252), (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40), (218, 87, 49), (174, 178, 231), (237, 169, 164), (6, 245, 223), (247, 9, 42)]

from  turtle  import  Turtle , Screen
turtle.colormode(255)
import random
tim = Turtle()
tim.up()
tim.hideturtle()
tim.speed("fastest")
tim.setheading(210)
tim.forward(400)
tim.setheading(0)
no_of_dots=100

for dot in range(1,no_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot%10==0:
        tim.left(90)
        tim.forward(50)
        tim.left(90)
        tim.forward(500)
        tim.right(180)


screen=Screen()
screen.exitonclick()