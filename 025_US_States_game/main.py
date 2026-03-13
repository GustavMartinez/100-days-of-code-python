import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. Statese Game")

image = "025_US_States_game/blank_states_img.gif" # Camino para la imagen
screen.addshape(image) # Adición de nueva forma 'shape' en el screen

turtle.shape(image) # Usar la imagen

# Código para identificar las coordenadas de cada punto de la imagen con un clic
def get_mouse_click_coor(x,y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)



# Logic
PATH_FILE = "/home/gustavo/Documents/programming/100-days-of-code-python/025_US_States_game/50_states.csv"
data = pd.read_csv(PATH_FILE)
all_states = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct", prompt="Cual es el estado?").title()
    print(answer_state)

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
