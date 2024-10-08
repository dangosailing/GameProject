import tkinter

root = tkinter.Tk()

root.geometry("1200x600")

info_display = tkinter.Label(root, background="green", bd=5, text="PLACEHOLDER: GAME EVENT INFORMATION")
player_display = tkinter.Label(root, background="blue", bd=5, text="PLACEHOLDER: Player name")
enemy_display = tkinter.Label(root, background="red", bd=5, text="PLACEHOLDER: Enemy name")

new_game_button = tkinter.Button(root, width=10, height=5, text="New Game")
save_button = tkinter.Button(root, width=10, height=5, text="Save")
load_button = tkinter.Button(root, width=10, height=5, text="Load")
quit_button = tkinter.Button(root, width=10, height=5, text="Quit")
attack_button = tkinter.Button(root, width=10, height=5, text="ATTACK")
defend_button = tkinter.Button(root, width=10, height=5, text="DEFEND")

info_display.place(relheight=0.5, relwidth=0.33, relx=.0)
player_display.place(relheight=0.5, relwidth=0.33, relx=.33)
enemy_display.place(relheight=0.5, relwidth=0.33, relx=.66)
new_game_button.place(relheight=0.1, relwidth=0.33, rely=.5)
save_button.place(relheight=0.1, relwidth=0.33, rely=.6)
load_button.place(relheight=0.1, relwidth=0.33, rely=.7)
quit_button.place(relheight=0.1, relwidth=0.33, rely=.8)


attack_button.place(relheight=0.1, relwidth=0.33, rely=.5, relx=0.33)
defend_button.place(relheight=0.1, relwidth=0.33, rely=.6, relx=0.33)

root.mainloop()