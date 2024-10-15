from datetime import datetime
from Game import Game
from GameUI import GameUI


class MainApp(Game, GameUI):
    """
    Class used to bind the game and the ui together
    """

    def __init__(self):
        Game.__init__(
            self
        )  # Multiple inheritance requires referencing each class instead of relying on super
        GameUI.__init__(self)

    def configure_button_methods(self) -> None:
        """
        Bind the button methods
        """
        self.button_new_game.config(command=self.initialize_game, state="active")
        self.button_quit.config(command=exit, state="active")
        self.button_new_round.config(command=self.initialize_round, state="active")
        self.button_attack.config(
            command=lambda: self.player_attack(attack_type="normal"), state="disabled"
        )
        self.button_strong_attack.config(
            command=lambda: self.player_attack(attack_type="strong"), state="disabled"
        )
        self.button_save_results.config(
            command=lambda: self.save_results(self.results), state="active"
        )
        self.button_create_character.config(
            command=self.initialize_character_creation, state="active"
        )
        self.plus_hp.config(command=lambda: self.add_to_stats(stat_type="hp"))
        self.minus_hp.config(command=lambda: self.subtract_from_stats(stat_type="hp"))
        self.plus_attack.config(command=lambda: self.add_to_stats(stat_type="attack"))
        self.minus_attack.config(
            command=lambda: self.subtract_from_stats(stat_type="attack")
        )
        self.plus_defense.config(command=lambda: self.add_to_stats(stat_type="defense"))
        self.minus_defense.config(
            command=lambda: self.subtract_from_stats(stat_type="defense")
        )
        self.plus_agility.config(command=lambda: self.add_to_stats(stat_type="agility"))
        self.minus_agility.config(
            command=lambda: self.subtract_from_stats(stat_type="agility")
        )

    def add_to_stats(self, stat_type: str) -> None:
        """
        Updates/Adds to player stats in increments of 10 from unallocated stat points
        """
        if self.player.unallocated_stat_pts == 0:
            self.remaining_pts_label.config(
                text=f"Remaining pts: {self.player.unallocated_stat_pts}\nNo more points to allocate"
            )
        else:
            if stat_type == "hp":
                new_hp = self.player.stats.get_hp() + 10
                self.player.stats.set_hp(new_hp)
                self.player.unallocated_stat_pts -= 10
                self.set_hp_label.config(text=f"HP: {self.player.stats.get_hp()}")
            if stat_type == "attack":
                new_attack = self.player.stats.get_attack() + 10
                self.player.stats.set_attack(new_attack)
                self.player.unallocated_stat_pts -= 10
                self.set_attack_label.config(
                    text=f"Attack: {self.player.stats.get_attack()}"
                )
            if stat_type == "defense":
                new_defense = self.player.stats.get_defense() + 10
                self.player.stats.set_defense(new_defense)
                self.player.unallocated_stat_pts -= 10
                self.set_defense_label.config(
                    text=f"Defense: {self.player.stats.get_defense()}"
                )
            if stat_type == "agility":
                new_agility = self.player.stats.get_agility() + 10
                self.player.stats.set_agility(new_agility)
                self.player.unallocated_stat_pts -= 10
                self.set_agility_label.config(
                    text=f"Agility: {self.player.stats.get_agility()}"
                )
            self.remaining_pts_label.config(
                text=f"Remaining pts: {self.player.unallocated_stat_pts}"
            )

    def subtract_from_stats(self, stat_type: str) -> None:
        """
        Updates/Removes player stats in increments of 10 and returns them to unallocated stat points
        """
        if stat_type == "hp":
            if self.player.stats.get_hp() <= 50:
                self.remaining_pts_label.config(
                    text=f"Remaining pts: {self.player.unallocated_stat_pts}\nHealth at minimum, can´t make it go lower"
                )
            else:
                new_hp = self.player.stats.get_hp() - 10
                self.player.stats.set_hp(new_hp)
                self.player.unallocated_stat_pts += 10
                self.set_hp_label.config(text=f"HP: {self.player.stats.get_hp()}")
                self.remaining_pts_label.config(
                    text=f"Remaining pts: {self.player.unallocated_stat_pts}"
                )

        if stat_type == "attack":
            if self.player.stats.get_attack() <= 10:
                self.remaining_pts_label.config(
                    text=f"Remaining pts: {self.player.unallocated_stat_pts}\nAttack at minimum, can´t make it go lower"
                )
            else:
                new_attack = self.player.stats.get_attack() - 10
                self.player.stats.set_attack(new_attack)
                self.player.unallocated_stat_pts += 10
                self.set_attack_label.config(
                    text=f"Attack: {self.player.stats.get_attack()}"
                )
                self.remaining_pts_label.config(
                    text=f"Remaining pts: {self.player.unallocated_stat_pts}"
                )

        if stat_type == "defense":
            if self.player.stats.get_defense() <= 0:
                self.remaining_pts_label.config(
                    text=f"Remaining pts: {self.player.unallocated_stat_pts}\nDefense at minimum, can´t make it go lower"
                )
            else:
                new_defense = self.player.stats.get_defense() - 10
                self.player.stats.set_defense(new_defense)
                self.player.unallocated_stat_pts += 10
                self.set_defense_label.config(
                    text=f"Defense: {self.player.stats.get_defense()}"
                )
                self.remaining_pts_label.config(
                    text=f"Remaining pts: {self.player.unallocated_stat_pts}"
                )

        if stat_type == "agility":
            if self.player.stats.get_agility() <= 0:
                self.remaining_pts_label.config(
                    text=f"Remaining pts: {self.player.unallocated_stat_pts}\nAgility at minimum, can´t make it go lower"
                )
            else:
                new_agility = self.player.stats.get_agility() - 10
                self.player.stats.set_agility(new_agility)
                self.player.unallocated_stat_pts += 10
                self.set_agility_label.config(
                    text=f"Agility: {self.player.stats.get_agility()}"
                )
                self.remaining_pts_label.config(
                    text=f"Remaining pts: {self.player.unallocated_stat_pts}"
                )

    def initialize_menu(self) -> None:
        """
        Initate the game with the start menu
        """
        self.create_widgets()
        self.configure_button_methods()
        self.render_game_frame()
        self.place_widgets_menu()
        self.root.mainloop()

    def initialize_character_creation(self) -> None:
        """
        Initate the game with the start menu
        """
        self.clear_game_frame()
        self.create_widgets()
        self.configure_button_methods()
        player_name = self.ask_player_name()
        self.create_characters(player_name=player_name)
        self.place_widgets_create_character(self.player)
        self.root.mainloop()

    def initialize_game(self) -> None:
        """
        Start a new game. Update ui elements with game session information
        """
        self.round_count = 0
        self.clear_game_frame()
        self.create_widgets()
        self.configure_button_methods()
        self.place_widgets_game()
        self.update_char_window(self.player)
        self.update_char_window(self.enemy)
        self.hp_bar_player.config(maximum=self.player.stats.get_hp() + 1)
        self.hp_bar_enemy.config(maximum=self.enemy.stats.get_hp() + 1)
        self.hp_bar_player.step(self.player.stats.get_hp())
        self.hp_bar_enemy.step(self.enemy.stats.get_hp())
        self.update_event_window("Welcome! Press start new round to begin")
        self.root.mainloop()

    def initialize_round(self) -> None:
        """
        Start a new round of the game. Increment round counter and update event window
        """
        self.round_count += 1
        self.update_event_window(f"Round {self.round_count}")
        self.button_new_round.config(
            state="disabled"
        )  # disable button when round starts to prevent player from disrupting game flow
        self.button_attack.config(state="active")
        self.button_strong_attack.config(state="active")

    def player_attack(self, attack_type: str) -> None:
        """
        Player attacks enemy with win game state check (in case enemy hp reaches 0)
        """
        enemy = self.enemy
        player = self.player
        if player.did_attack_hit(enemy.stats.get_agility()):
            if attack_type == "normal":
                attack_damage = player.attack(
                    opponent_defense=enemy.stats.get_defense()
                )
            elif attack_type == "strong":
                attack_damage = player.strong_attack()
            else:
                attack_damage = 0  # In case attack skill is not properly implemented the attack value is set to 0
            if attack_damage > 0:
                enemy.stats.set_hp(enemy.stats.get_hp() - attack_damage)
                self.hp_bar_enemy.step(-attack_damage)
                event_msg = f"You attacked! {enemy.get_name()} took damage. {enemy.stats.get_hp()} HP remaining"
            else:
                event_msg = f"You attacked but {enemy.get_name()} took no damage. The attack was too weak!"
            self.update_event_window(event_msg)
            if self.check_win_state():
                results = f"{self.player.get_name()} bested {self.enemy.get_name()} in {self.round_count} rounds"
                self.game_over(results)
            self.update_char_window(enemy)
        else:
            event_msg = "Your attack missed. The enemy was too nimble!"
            self.update_event_window(event_msg)
        self.button_attack.config(state="disabled")
        self.button_strong_attack.config(state="disabled")
        self.enemy_attack()

    def enemy_attack(self) -> None:
        """
        Enemy attacks player with fail game state check (in case player hp reaches 0)
        """
        enemy = self.enemy
        player = self.player
        if enemy.did_attack_hit(player.stats.get_agility()):
            attack_damage = enemy.attack(opponent_defense=player.stats.get_defense())
            if attack_damage > 0:
                player.stats.set_hp(player.stats.get_hp() - attack_damage)
                self.hp_bar_player.step(-attack_damage)
                event_msg = f"{player.get_name()} took damage. {player.stats.get_hp()} HP remaining"
            else:
                event_msg = (
                    f"{player.get_name()} took no damage. The attack was too weak!"
                )
            self.update_event_window(event_msg)
            if self.check_fail_state():
                results = f"{self.enemy.get_name()} bested {self.player.get_name()} in {self.round_count} rounds"
                self.game_over(results)
            self.update_char_window(player)
        else:
            event_msg = f"{enemy.get_name()}´s attack missed. You got lucky!"
            self.update_event_window(event_msg)
        self.button_new_round.config(state="active")

    def game_over(self, results: str) -> None:
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

    def save_results(self, results: str) -> None:
        """
        Save game session results to text file
        """
        now = datetime.now().strftime("%H:%M:%S")
        save_text = f"{now} - {results}\n"
        with open("results.txt", "a") as file:
            file.write(save_text)
            self.button_save_results.config(state="disabled")
        self.score_screen()



# ----- Run program ----- #

new_game = MainApp()
new_game.initialize_menu()

# ----------------------- #
