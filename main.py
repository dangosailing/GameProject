from Game import Game
from Game_UI import Game_UI
from tkinter import simpledialog

class Main(Game, Game_UI):
    """
    Class used to bind the game and the ui together
    """
    def __init__(self):
        Game.__init__(self) # Multiple inheritance requires referencing each class instead of relying on super
        Game_UI.__init__(self)
    
    def configure_button_methods(self):
        self.button_new_game.config(command = self.initialize_game, state="active")
        self.button_quit.config(command = exit, state="active")
        self.button_new_round.config(command = self.initialize_round, state="active")
        self.button_attack.config(command = lambda: self.player_attack(), state="disabled")
        
    def initialize_menu(self):
        self.create_widgets()
        self.configure_button_methods()
        self.render_game_frame()
        self.place_widgets_menu()
        self.root.mainloop()

    def initialize_game(self):
        player_name = simpledialog.askstring("Enter Player Name", "Enter your character´s name", parent=self.game_frame)
        self.game_active = True
        self.create_characters(player_name=player_name)
        self.clear_game_frame()
        self.create_widgets()
        self.configure_button_methods()
        self.place_widgets_game()
        self.update_char_window(self.player)
        self.update_char_window(self.enemy)
        self.initialize_round()
        self.root.mainloop()

    def initialize_round(self):
        self.round_count += 1
        self.update_event_window(f"Round {self.round_count}")
        self.play_turn()

    def play_turn(self):
        self.player_active = True
        self.button_attack.config(state="active")
        self.button_new_round.config(state="disabled") # disable button when round starts to prevent player from disrupting game flow
        self.update_event_window(f"Player turn, use an action to advance the round")
            
    def player_attack(self) -> None:
        enemy = self.enemy
        player = self.player 

        # ------------------ Player moves ------------------ #
        attack_damage = player.attack(opponent_defense=enemy.stats.get_defense())
        if attack_damage > 0:
            enemy.stats.set_hp(enemy.stats.get_hp() - attack_damage)
            event_msg = f"You attacked! {enemy.get_name()} took damage. {enemy.stats.get_hp()} HP remaining"
        else:
            event_msg = f"You attacked but {enemy.get_name()} took no damage. The attack was too weak!"
        self.update_event_window(event_msg)
        if self.check_win_state():
            event_msg = "Congratulations you have slain your enemy!"
            self.game_over(event_msg)


        # ------------------ Enemy moves ------------------ #
        attack_damage = enemy.attack(opponent_defense=player.stats.get_defense())
        if attack_damage > 0:
            player.stats.set_hp(player.stats.get_hp() - attack_damage)
            event_msg = f"{player.get_name()} took damage. {player.stats.get_hp()} HP remaining"
        else:
            event_msg = f"{player.get_name()} took no damage. The attack was too weak!"
        self.update_event_window(event_msg)
        if self.check_fail_state():
            event_msg = "Oh no! Your enemy has defeated you"
            self.game_over(event_msg)

        # ------------------ Reset turn parameters ------------------ #
        self.player_active = False
        self.button_attack.config(state="disabled")
        self.button_new_round.config(state="active") # disable button when round starts to prevent player from disrupting game flow

        self.update_char_window(enemy)
        self.update_char_window(player)
        self.update_event_window("Round over!")
        self.initialize_round()

    def game_over(self, event_msg:str):
        self.button_attack.config(state="disabled")        
        self.button_new_round.config(state="disabled")        
        self.clear_game_frame()
        self.create_widgets()
        self.render_game_over(event_msg)
        self.game_active = False



  
        
    
                    
    
new_game = Main()
new_game.initialize_menu()



"""
Add a round count that tracks number of rounds the battle takes

When game starts display a message telling player to start new round.
Only thing player can do when game starts is to start a new round or quit game.

When new round starts add to round count and display round number in event window



Complete one round in game

When round is initiated, disable new round button
When round is over, ie not initiated, disable attack button

A round consists of an attack from a player and one from an enemy
Use speed to determine who goes first

Use a conditional if statement to determine who goes first and who goes last using the speed attribute
Use a variable to save who goes first and who goes last

Calculate damage value using class method attack

"""