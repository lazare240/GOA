from turtle import *
# we want to pante house
# step 1: drawing a spuare
speed(0.1)

width (1)
forward (200)
left (90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

# end of spuare
#drawing a door
begin_fill()
forward(70)
color("blue")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()

color("green")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(60,150)
pendown()

color("red")
begin_fill()
right(60)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
right(60)
end_fill()

penup()
goto(180,150)
pendown()

color("yellow")
begin_fill()
right(120)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
right(120)
left(210)
forward(40)
end_fill()

penup()
goto(10,220)
pendown()

exitonclick()