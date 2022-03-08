import turtle
import pandas

screen = turtle.Screen()
screen.title("India States Game")
image = "india_map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("india_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 28:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/28 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.shape("circle")
        t.shapesize(0.3, 0.3)
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
