from Character import Character
from CharacterStats import CharacterStats


class Game:
    """
    Class to define Game attribute and methods
    """

    def __init__(self) -> None:
        self.player = None
        self.enemy = None
        self.round_count = 0
        self.results = ""

    def create_characters(self, player_name: str) -> None:
        """
        Ask player to create their character and select an enemy
        """
        enemy_name = "Goblin King"  # Placeholder name

        warrior_stats = CharacterStats(hp=50, attack=20, defense=10, agility=10)
        warrior = Character(name=player_name, stats=warrior_stats, is_player=True)

        enemy_stats = CharacterStats(hp=150, attack=25, defense=2, agility=20)
        enemy = Character(name=enemy_name, stats=enemy_stats, is_player=False)

        self.player = warrior
        self.enemy = enemy

    def check_win_state(self) -> bool:
        """
        Used to check if game has entered a win state.
        """
        if self.enemy.stats.get_hp() <= 0:
            return True
        else:
            return False

    def check_fail_state(self) -> bool:
        """
        Used to check if game has entered a fail state.
        """
        if self.player.stats.get_hp() <= 0:
            return True
        else:
            return False
