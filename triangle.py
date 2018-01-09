import turtle

painter = turtle.Turtle()
painter.pencolor("purple")
#Should this actually be red?
#YOu are right, should be purple

for _ in range(13):
	painter.forward(100)
	painter.left(140)
	painter.backward(20)
	painter.right(30) 

turtle.done()
