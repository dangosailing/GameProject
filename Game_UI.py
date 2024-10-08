from tkinter import Tk, simpledialog, Button, Entry, Frame, BOTH, Label
from Game import Game

class Game_UI(Game):
    """
    Game UI class that contains the methods used to render information from the game to the player
    """
    def __init__(self) -> None:
        super().__init__()
        self.root = Tk()
        self.game_frame = Frame(self.root, bg="black") # Creating a frame to make it easer to wipe it once i want to transition from main menu into game 
        self.info_display = None # Used to easier get access from within methods
        self.player_display = None # Used to easier get access from within methods
        self.enemy_display = None # Used to easier get access from within methods
        self.quit_button = None # Used to easier get access from within methods
        self.new_game_button = None # Used to easier get access from within methods
        self.attack_button = None # Used to easier get access from within methods
        self.defend_button = None # Used to easier get access from within methods
        
        
    def clear_game_frame(self, frame:Frame) -> None:
        """
        Clears the game frame from elements
        """
        for widget in frame.winfo_children():
            widget.destroy()

    def update_info_window(self, text) -> None:
        """
        Updates the game log display with new information
        """
        self.info_display.config(text=text)

    def render_game_screen(self, frame:Frame) -> None:
        """
        Renders the initial game window when starting the game from the menu
        """
        self.info_display = Label(frame, background="darkgrey", bd=5, text="PLACEHOLDER: GAME EVENT INFORMATION")
        self.player_display = Label(frame, background="blue", bd=5, text="PLACEHOLDER: Player name")
        self.enemy_display = Label(frame, background="red", bd=5, text="PLACEHOLDER: Enemy name")
        self.info_display.place(relheight=0.5, relwidth=0.33, relx=.0)
        self.player_display.place(relheight=0.5, relwidth=0.33, relx=.33)
        self.enemy_display.place(relheight=0.5, relwidth=0.33, relx=.66)
        
        self.quit_button = Button(frame, text="Quit Game", command=exit) # Game needs a Quit button always available since the game is fullscreen
        self.save_button = Button(frame, text="Save", command=lambda: self.update_info_window("SAVING")) # Placeholder to test window update method. Lamda here is used to create an anonymous function that we can pass our function to. This is done to allow for text to passed as an argument to the callback function
        self.attack_button = Button(frame, text="ATTACK",  command=lambda: self.update_info_window("PLAYER ATTACKING"))
        self.defend_button = Button(frame, text="DEFEND",  command=lambda: self.update_info_window("PLAYER DEFENDING"))
        
        self.save_button.place(relheight=0.1, relwidth=0.33, rely=.5)
        self.quit_button.place(relheight=0.1, relwidth=0.33, rely=.6)
        self.attack_button.place(relheight=0.1, relwidth=0.33, rely=.5, relx=0.33)
        self.defend_button.place(relheight=0.1, relwidth=0.33, rely=.6, relx=0.33)


    def new_game(self) -> None:
        """
        Clears game menu window and loads the render method for the game window
        """
        self.clear_game_frame(self.game_frame)
        self.render_game_screen(self.game_frame)

    def render_menu(self) -> None:
        """
        Renders the initial game menu window
        """
        self.root.attributes('-fullscreen',True) # Sets the main root window fo fullscreen
        self.game_frame.pack(expand=1, fill=BOTH) # Sets the game frame to expand into fullscreen
        new_game_button = Button(self.game_frame, text="New Game", command=self.new_game)
        quit_button = Button(self.game_frame, text="Quit", command=exit) # Game needs a Quit button always available since the game is fullscreen
        new_game_button.place(relheight=0.1, relwidth=0.33, rely=.5, relx=0)
        quit_button.place(relheight=0.1, relwidth=0.33, rely=.6, relx=0)
        self.root.mainloop()