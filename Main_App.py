from Game import Game
from Game_UI import Game_UI
from datetime import datetime

class Main_App(Game, Game_UI):
    """
    Class used to bind the game and the ui together
    """
    def __init__(self):
        Game.__init__(self) # Multiple inheritance requires referencing each class instead of relying on super
        Game_UI.__init__(self)
    
    def configure_button_methods(self) -> None:
        """
        Bind the button methods
        """
        self.button_new_game.config(command = self.initialize_game, state="active")
        self.button_quit.config(command = exit, state="active")
        self.button_new_round.config(command = self.initialize_round, state="active")
        self.button_attack.config(command = lambda: self.player_attack(attack_type="normal"), state="disabled")
        self.button_strong_attack.config(command = lambda: self.player_attack(attack_type="strong"), state="disabled")
        self.button_save_results.config(command = lambda: self.save_results(self.results), state="active")
        
    def initialize_menu(self) -> None:
        """
        Initate the game with the start menu
        """
        self.create_widgets()
        self.configure_button_methods()
        self.render_game_frame()
        self.place_widgets_menu()
        self.root.mainloop()

    def initialize_game(self) -> None:
        """
        Start a new game. Update ui elements with game session information
        """
        player_name = self.ask_player_name()
        self.game_active = True
        self.create_characters(player_name=player_name)
        self.clear_game_frame()
        self.create_widgets()
        self.configure_button_methods()
        self.place_widgets_game()
        self.update_char_window(self.player)
        self.update_char_window(self.enemy)
        self.hp_bar_player.config(maximum=self.player.stats.get_hp()+1)  # The progressbar resets at 100% filled, so for us to use it we add a small value to the max to make sure it can render at "max hp"
        self.hp_bar_enemy.config(maximum=self.enemy.stats.get_hp()+1) 
        self.hp_bar_player.step(self.player.stats.get_hp()) # Set the progressbar to equal max hp at start of game
        self.hp_bar_enemy.step(self.enemy.stats.get_hp())
        self.update_event_window(f"Welcome! Press start new round to begin")
        self.root.mainloop()

    def initialize_round(self) -> None:
        """
        Start a new round of the game. Increment round counter and update event window
        """
        self.round_count += 1
        self.player_moved = False
        self.player_moved = False
        self.update_event_window(f"Round {self.round_count}")
        self.play_turn()


# TODO : FIGURE OUT WHY ENEMY IS ATTACKING AT FIRST ROUND AND THEN NEVER AGAIN
    def play_turn(self) -> None:
        """
        Use speed stat to determine who goes first and activate relevant ui elements to enable/disable player turn
        """
        self.button_new_round.config(state="disabled") # disable button when round starts to prevent player from disrupting game flow
        #if self.player_moved == False and self.enemy_moved == False:
        if self.player.stats.get_speed() > self.enemy.stats.get_speed():
            self.update_event_window("You get the first move!")
            self.player_active = True
            self.button_attack.config(state="active")
            self.button_strong_attack.config(state="active")
        else:
            self.update_event_window("Your enemy gets the first move! They chose to attack")
            self.enemy_attack()
            self.update_event_window(f"Playxer turn, use an action to advance the round")
            self.player_active = True
            self.button_attack.config(state="active")
            self.button_strong_attack.config(state="active")
        if self.enemy_moved == False:
            self.enemy_attack()
            
    def player_attack(self, attack_type:str) -> None:
        """
        Player attacks enemy with win game state check (in case enemy hp reaches 0)
        """
        enemy = self.enemy
        player = self.player 
        if attack_type == "normal":
            attack_damage = player.attack(opponent_defense=enemy.stats.get_defense())
        elif attack_type == "strong":
            attack_damage = player.strong_attack()
        if attack_damage > 0:
            enemy.stats.set_hp(enemy.stats.get_hp() - attack_damage)
            self.hp_bar_enemy.step(-attack_damage) # The progressbar is set to equal the max hp so we just need to subtract the attack damage as step size
            event_msg = f"You attacked! {enemy.get_name()} took damage. {enemy.stats.get_hp()} HP remaining"
        else:
            event_msg = f"You attacked but {enemy.get_name()} took no damage. The attack was too weak!"
        self.update_event_window(event_msg)
        if self.check_win_state():
            results = f"{self.player.get_name()} bested {self.enemy.get_name()} in {self.round_count} rounds"
            self.game_over(results)
        self.update_char_window(enemy)
        self.player_active = False
        self.button_attack.config(state="disabled")
        self.button_strong_attack.config(state="disabled")
        self.button_new_round.config(state="active")
        self.player_moved = True

    def enemy_attack(self) -> None:
        """
        Enemy attackss player with fail game state check (in case player hp reaches 0)
        """
        enemy = self.enemy
        player = self.player 
        attack_damage = enemy.attack(opponent_defense=player.stats.get_defense())
        if attack_damage > 0:
            player.stats.set_hp(player.stats.get_hp() - attack_damage)
            self.hp_bar_player.step(-attack_damage) # The progressbar is set to equal the max hp so we just need to subtract the attack damage as step size
            event_msg = f"{player.get_name()} took damage. {player.stats.get_hp()} HP remaining"
        else:
            event_msg = f"{player.get_name()} took no damage. The attack was too weak!"
        self.update_event_window(event_msg)
        if self.check_fail_state():
            results = f"{self.enemy.get_name()} bested {self.player.get_name()} in {self.round_count} rounds"
            self.game_over(results)
        self.update_char_window(player)
        self.player_active = True
        self.enemy_moved = True
        
    def game_over(self, results:str) -> None:
        """
        Activate game over menu
        """
        self.results = results
        self.button_attack.config(state="disabled")        
        self.button_strong_attack.config(state="disabled")        
        self.button_new_round.config(state="disabled")        
        self.clear_game_frame()
        self.create_widgets()
        self.render_game_over(results)
        self.configure_button_methods()
        self.game_active = False
    
    def save_results(self, results:str) -> None:    
        """
        Save game session results to text file
        """
        now = datetime.now().strftime("%H:%M:%S")   
        save_text = f"{now} - {results}\n"
        with open("results.txt", "a") as file:
            file.write(save_text)
            self.button_save_results.config(state="disabled")
        self.score_screen()

new_game = Main_App()
new_game.initialize_menu()

