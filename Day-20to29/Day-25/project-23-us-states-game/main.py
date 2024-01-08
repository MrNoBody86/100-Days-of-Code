import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S States Game")
image = "Day-20to29\Day-25\project-23-us-states-game\\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("Day-20to29\Day-25\project-23-us-states-game\\50_states.csv")

guessed_state = []
answer_state = screen.textinput(title="Guess the State",prompt="What's state's name?").title()
while len(guessed_state) < 50 :
    state_list = data.state.to_list()
    if answer_state == "Exit":
        remaining_states = []
        for state in state_list:
            if state not in guessed_state:
                remaining_states.append(state)

        new_data = pandas.DataFrame(remaining_states)
        new_data.to_csv("Day-20to29\Day-25\project-23-us-states-game\missing_states.csv")
        break
    if answer_state in state_list:
        state_data = data[data.state == answer_state]
        x = int(state_data.x)
        y = int(state_data.y)
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        tim.goto(x,y)
        tim.write(str(answer_state),align="center")
        guessed_state.append(answer_state)
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Guessed",prompt="What's another state's name?").title()


