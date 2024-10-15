from os import path
from tkinter import Tk, Button, Frame, BOTH, Label, Listbox, simpledialog, ttk
from datetime import datetime
from Character import Character


class GameUI:
    """
    Game UI class that contains the methods used to render information from the game to the player
    """

    def __init__(self) -> None:
        self.root = Tk()
        self.game_frame = Frame(
            self.root, bg="black"
        )  # Creating a frame to make it easer to wipe it once i want to transition from main menu into game
        self.window_event = None  # Used to easier get access from within methods
        self.window_player = None  # Used to easier get access from within methods
        self.window_enemy = None  # Used to easier get access from within methods
        self.button_quit = None  # Used to easier get access from within methods
        self.button_save_results = None  # Used to easier get access from within methods
        self.button_new_game = None  # Used to easier get access from within methods
        self.button_create_character = (
            None  # Used to easier get access from within methods
        )
        self.button_attack = None  # Used to easier get access from within methods
        self.button_strong_attack = (
            None  # Used to easier get access from within methods
        )
        self.button_new_round = None  # Used to easier get access from within methods
        self.dialog_enter_name = None  # Used to easier get access from within methods
        self.game_over_label_1 = None  # Used to easier get access from within methods
        self.game_over_label_2 = None  # Used to easier get access from within methods
        self.button_use_skill = None  # Used to easier get access from within methods
        self.hp_bar_player = None  # Used to easier get access from within methods
        self.hp_bar_enemy = None  # Used to easier get access from within methods
        self.set_hp_label = None  # Used to easier get access from within methods
        self.set_attack_label = None  # Used to easier get access from within methods
        self.set_defense_label = None  # Used to easier get access from within methods
        self.set_agility_label = None  # Used to easier get access from within methods
        self.plus_hp = None  # Used to easier get access from within methods
        self.minus_hp = None  # Used to easier get access from within methods
        self.plus_attack = None  # Used to easier get access from within methods
        self.minus_attack = None  # Used to easier get access from within methods
        self.plus_defense = None  # Used to easier get access from within methods
        self.minus_defense = None  # Used to easier get access from within methods
        self.plus_agility = None  # Used to easier get access from within methods
        self.minus_agility = None  # Used to easier get access from within methods
        self.remaining_pts_label = None

    def score_screen(self) -> None:
        """
        Read results file and render a seperate score window
        """
        score_window = Tk()
        score_window.geometry("600x600")
        score_window.title("Memories of previous victories")
        scores = Listbox(
            score_window, background="black", bd=5, fg="white", state="normal"
        )
        scores.place(relwidth=1, relheight=1)
        if path.isfile("results.txt"):
            with open("results.txt", "r") as file:
                entries = file.readlines()
                for entry in entries:
                    scores.insert(0, entry.strip())

    def clear_game_frame(self) -> None:
        """
        Clears the game frame from elements
        """
        for widget in self.game_frame.winfo_children():
            widget.destroy()

    def update_event_window(self, event_message: str) -> None:
        """
        Updates the game log display with new information and a timestamp
        """
        timestamp_event = datetime.now().strftime("%H:%M:%S")
        self.window_event.insert(0, f"{timestamp_event} - {event_message}")

    def update_char_window(self, character: Character) -> None:
        """
        Updates the game log display with new information and a timestamp
        """
        stats = character.stats
        name = character.get_name()
        health = stats.get_hp()
        attack = stats.get_attack()
        agility = stats.get_agility()
        defense = stats.get_defense()
        status_text = f"{name}\nHealth:{health}\nAttack: {attack}\nDefense: {defense}\nAgility: {agility}"
        if character.is_player:
            self.window_player.config(text=status_text)
        else:
            self.window_enemy.config(text=status_text)

    def create_widgets(self) -> None:
        """
        Creates and sets the widgets without methods. Widgets methods are assigned in the Main class
        """
        self.root.title("Fate of the fury")
        self.window_event = Listbox(
            self.game_frame, background="black", bd=5, fg="white", state="normal"
        )
        self.window_player = Label(
            self.game_frame,
            background="white",
            bd=5,
            text="PLACEHOLDER: Player name",
            fg="black",
        )
        self.window_enemy = Label(
            self.game_frame, background="red", bd=5, text="PLACEHOLDER: Enemy name"
        )
        self.button_quit = Button(self.game_frame, text="Quit Game")
        self.button_save_results = Button(self.game_frame, text="Save results")
        self.button_new_round = Button(self.game_frame, text="NEW ROUND")
        self.button_attack = Button(self.game_frame, text="ATTACK")
        self.button_strong_attack = Button(self.game_frame, text="STRONG ATTACK")
        self.button_new_game = Button(self.game_frame, text="New Game")
        self.button_create_character = Button(self.game_frame, text="Create character")
        self.button_quit = Button(self.game_frame, text="Quit", command=exit)
        self.game_over_label_1 = Label(
            self.game_frame,
            text="Game Over",
            bg="black",
            fg="white",
            font=("Arial", 25),
        )
        self.game_over_label_2 = Label(self.game_frame, text="", bg="black", fg="white")
        self.hp_bar_player = ttk.Progressbar(self.game_frame)
        self.hp_bar_enemy = ttk.Progressbar(self.game_frame)
        self.remaining_pts_label = Label(
            self.game_frame, background="white", bd=5, fg="black"
        )
        self.set_hp_label = Label(self.game_frame, background="white", bd=5, fg="black")
        self.set_attack_label = Label(
            self.game_frame, background="white", bd=5, fg="black"
        )
        self.set_defense_label = Label(
            self.game_frame, background="white", bd=5, fg="black"
        )
        self.set_agility_label = Label(
            self.game_frame, background="white", bd=5, fg="black"
        )
        self.plus_hp = Button(self.game_frame, text="+")
        self.minus_hp = Button(self.game_frame, text="-")
        self.plus_attack = Button(self.game_frame, text="+")
        self.minus_attack = Button(self.game_frame, text="-")
        self.plus_defense = Button(self.game_frame, text="+")
        self.minus_defense = Button(self.game_frame, text="-")
        self.plus_agility = Button(self.game_frame, text="+")
        self.minus_agility = Button(self.game_frame, text="-")

    def place_widgets_game(self) -> None:
        """
        Places widgets in the game frame
        """
        self.window_event.place(relheight=0.5, relwidth=0.33, relx=0.0)
        self.window_player.place(relheight=0.5, relwidth=0.33, relx=0.33)
        self.window_enemy.place(relheight=0.5, relwidth=0.33, relx=0.66)

        self.hp_bar_player.place(relheight=0.04, relwidth=0.33, relx=0.33)
        self.hp_bar_enemy.place(relheight=0.04, relwidth=0.33, relx=0.66)

        self.button_quit.place(relheight=0.1, relwidth=0.33, rely=0.5)
        self.button_new_round.place(relheight=0.1, relwidth=0.33, rely=0.5, relx=0.33)
        self.button_attack.place(relheight=0.1, relwidth=0.33, rely=0.5, relx=0.66)
        self.button_strong_attack.place(
            relheight=0.1, relwidth=0.33, rely=0.6, relx=0.66
        )

    def render_game_frame(self) -> None:
        """
        Set root window to full screen and make the game frame expand to fill it
        """
        self.root.attributes(
            "-fullscreen", True
        )  # Sets the main root window fo fullscreen
        self.game_frame.pack(
            expand=1, fill=BOTH
        )  # Sets the game frame to expand into fullscreen

    def place_widgets_menu(self) -> None:
        """
        Places widgets in the menu frame
        """
        self.button_create_character.place(
            relheight=0.1, relwidth=0.33, rely=0.5, relx=0
        )
        self.button_quit.place(relheight=0.1, relwidth=0.33, rely=0.6, relx=0)

    def render_game_over(self, results: str) -> None:
        """
        Render game over screen
        """
        self.game_over_label_2.config(text=results)
        self.game_over_label_1.place(relheight=0.1, relwidth=0.33, rely=0.3, relx=0.33)
        self.game_over_label_2.place(relheight=0.1, relwidth=0.33, rely=0.4, relx=0.33)
        self.button_create_character.place(
            relheight=0.1, relwidth=0.33, rely=0.5, relx=0.33
        )
        self.button_save_results.place(
            relheight=0.1, relwidth=0.33, rely=0.6, relx=0.33
        )
        self.button_quit.place(relheight=0.1, relwidth=0.33, rely=0.7, relx=0.33)

    def ask_player_name(self) -> str:
        """
        Render a dialog box with player name input. Returns player name as string
        """
        player_name = simpledialog.askstring(
            "Enter Player Name", "Enter your character´s name", parent=self.game_frame
        )
        return player_name

    def place_widgets_create_character(self, player: Character) -> None:
        """
        Render a character creator screen
        """
        standard_hp = player.stats.get_hp()
        standard_attack = player.stats.get_attack()
        standard_defense = player.stats.get_defense()
        standard_agility = player.stats.get_agility()
        remaining_stat_pts = player.unallocated_stat_pts

        self.remaining_pts_label.config(text=f"Remaining pts: {remaining_stat_pts}")
        self.set_hp_label.config(text=f"HP: {standard_hp}")
        self.set_attack_label.config(text=f"Attack: {standard_attack}")
        self.set_defense_label.config(text=f"Defense: {standard_defense}")
        self.set_agility_label.config(text=f"Agility: {standard_agility}")

        self.remaining_pts_label.place(relheight=0.1, relwidth=0.33, rely=0.2, relx=0.5)
        self.plus_hp.place(relheight=0.1, relwidth=0.05, rely=0.3, relx=0.5)
        self.minus_hp.place(relheight=0.1, relwidth=0.05, rely=0.3, relx=0.56)
        self.plus_attack.place(relheight=0.1, relwidth=0.05, rely=0.4, relx=0.5)
        self.minus_attack.place(relheight=0.1, relwidth=0.05, rely=0.4, relx=0.56)
        self.plus_defense.place(relheight=0.1, relwidth=0.05, rely=0.5, relx=0.5)
        self.minus_defense.place(relheight=0.1, relwidth=0.05, rely=0.5, relx=0.56)
        self.plus_agility.place(relheight=0.1, relwidth=0.05, rely=0.6, relx=0.5)
        self.minus_agility.place(relheight=0.1, relwidth=0.05, rely=0.6, relx=0.56)
        self.set_hp_label.place(relheight=0.1, relwidth=0.33, rely=0.3, relx=0.1)
        self.set_attack_label.place(relheight=0.1, relwidth=0.33, rely=0.4, relx=0.1)
        self.set_defense_label.place(relheight=0.1, relwidth=0.33, rely=0.5, relx=0.1)
        self.set_agility_label.place(relheight=0.1, relwidth=0.33, rely=0.6, relx=0.1)

        self.button_new_game.place(relheight=0.1, relwidth=0.33, rely=0.7, relx=0.1)
        self.button_quit.place(relheight=0.1, relwidth=0.33, rely=0.8, relx=0.1)
