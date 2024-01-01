from turtle import Turtle , Screen

tim = Turtle()
screen = Screen()

def moveforward():
    tim.fd(10)

def movebackward():
    tim.bk(10)

def movecolckwise():
    tim.rt(10)

def moveanticolckwise():
    tim.lt(10)

def clearscreen():
    tim.reset()

screen.listen()
screen.onkeypress(key="w",fun=moveforward)
screen.onkeypress(key="s",fun=movebackward)
screen.onkeypress(key="a",fun=moveanticolckwise)
screen.onkeypress(key="d",fun=movecolckwise)
screen.onkeypress(key="c",fun=clearscreen)

screen.exitonclick()


