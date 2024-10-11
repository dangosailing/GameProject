from Game import Game
from Game_UI import Game_UI
from tkinter import simpledialog
from datetime import datetime

class Main_App(Game, Game_UI):
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
        self.button_save_results.config(command = lambda: self.save_results(self.results), state="active")
        
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
        self.update_event_window(f"Welcome! Press start new round to begin")
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
            results = f"{self.player.get_name()} bested {self.enemy.get_name()} in {self.round_count} rounds"
            self.game_over(results)

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

    def game_over(self, results:str):
        self.results = results
        self.button_attack.config(state="disabled")        
        self.button_new_round.config(state="disabled")        
        self.clear_game_frame()
        self.create_widgets()
        self.render_game_over(results)
        self.configure_button_methods()
        self.game_active = False
    
    def save_results(self, results:str):     
        now = datetime.now().strftime("%H:%M:%S")   
        save_text = f"{now} - {results}\n"
        with open("results.txt", "a") as file:
            file.write(save_text)
            self.button_save_results.config(state="disabled")
        self.score_screen()

new_game = Main_App()
new_game.initialize_menu()