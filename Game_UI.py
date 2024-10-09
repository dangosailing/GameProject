from tkinter import Tk, Button, Frame, BOTH, Label, Listbox
from datetime import datetime

class Game_UI:
    """
    Game UI class that contains the methods used to render information from the game to the player
    """
    def __init__(self) -> None:
        self.root = Tk()
        self.game_frame = Frame(self.root, bg="black") # Creating a frame to make it easer to wipe it once i want to transition from main menu into game 
        self.display_info = None # Used to easier get access from within methods
        self.display_player = None # Used to easier get access from within methods
        self.display_enemy = None # Used to easier get access from within methods
        self.button_quit = None # Used to easier get access from within methods
        self.button_new_game = None # Used to easier get access from within methods
        self.button_attack = None # Used to easier get access from within methods
        self.button_new_round = None # Used to easier get access from within methods
        
    def clear_game_frame(self) -> None:
        """
        Clears the game frame from elements
        """
        for widget in self.game_frame.winfo_children():
            widget.destroy()

    def update_info_window(self, event_message:str) -> None:
        """
        Updates the game log display with new information and a timestamp
        """
        timestamp_event = datetime.now().strftime("%H:%M:%S")
        self.display_info.insert(0, f"{timestamp_event} - {event_message}")

    def create_widgets(self) -> None:
        """
        Creates and sets the widgets without methods. Widgets methods are assigned in the Main class
        """
        self.display_info = Listbox(self.game_frame, background="darkgrey", bd=5)
        self.display_player = Label(self.game_frame, background="white", bd=5, text="PLACEHOLDER: Player name")
        self.display_enemy = Label(self.game_frame, background="red", bd=5, text="PLACEHOLDER: Enemy name")
        self.button_quit = Button(self.game_frame, text="Quit Game")
        self.button_new_round = Button(self.game_frame, text="NEW ROUND")
        self.button_attack = Button(self.game_frame, text="ATTACK")
        self.button_new_game = Button(self.game_frame, text="New Game")
        self.button_quit = Button(self.game_frame, text="Quit", command=exit)


    def place_widgets_game(self) -> None:
        """
        Places widgets in the game frame
        """
        self.display_info.place(relheight=0.5, relwidth=0.33, relx=.0)
        self.display_player.place(relheight=0.5, relwidth=0.33, relx=.33)
        self.display_enemy.place(relheight=0.5, relwidth=0.33, relx=.66)    
        
        self.button_quit.place(relheight=.1, relwidth=.33, rely=.5)
        self.button_new_round.place(relheight=.1, relwidth=.33, rely=.5, relx=.33)
        self.button_attack.place(relheight=.1, relwidth=.33, rely=.5, relx=.66)
        

    def render_game_frame(self):
        """
        Set root window to full screen and make the game frame expand to fill it
        """
        self.root.attributes('-fullscreen',True) # Sets the main root window fo fullscreen
        self.game_frame.pack(expand=1, fill=BOTH) # Sets the game frame to expand into fullscreen

    def place_widgets_menu(self) -> None:
        """
        Places widgets in the menu frame
        """
        self.button_new_game.place(relheight=0.1, relwidth=0.33, rely=.5, relx=0)
        self.button_quit.place(relheight=0.1, relwidth=0.33, rely=.6, relx=0)

