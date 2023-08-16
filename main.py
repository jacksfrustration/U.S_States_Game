import pandas as pd
import turtle as tur

states_data=pd.read_csv("50_states.csv")
screen=tur.Screen()
screen.setup(750,500)
screen.bgpic("blank_states_img.gif")
state_names_list=list(states_data["state"])
guessed_states=[]
while state_names_list:
    answer=screen.textinput(title=f"{len(guessed_states)}/50 guessed:",prompt="Guess a state: ").title()

    if answer.title() in state_names_list:
        state_names_list.remove(answer)
        guessed_states.append(answer)
        new_x=states_data[states_data.state==answer].x.item()
        new_y=states_data[states_data.state==answer].y.item()
        guessed_state=tur.Turtle()
        guessed_state.penup()
        guessed_state.goto(x=new_x,y=new_y)
        guessed_state.write(answer)

print("You have guessed all of the states")
screen.exitonclick()
