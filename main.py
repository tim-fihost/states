import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image) #check extensions 

turtle.shape(image)

guessed = []

while len(guessed) < 50:
    answer_state = screen.textinput(title=f"{len(guessed)} \ 50 States Correct", 
                                    prompt="Your input:").title()
    #Read CSV
    data = pandas.read_csv("50_states.csv")
    all_states = data.state.to_list()
    #Create a loop
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guessed.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)

not_guessed = []

for i in data.state:
    if i not in guessed:
        not_guessed.append(i)

df = pandas.DataFrame(not_guessed)
df.to_csv("not_guessed.csv")