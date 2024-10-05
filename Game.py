from Character import Character
from Character_Stats import Character_Stats

class Game:
  """
  Class to define Game attribute and methods
  """
  def __init__(self, player:Character, enemy:Character) -> None:
    self.player = player
    self.enemy = enemy

  def display_information(self, text:str) -> None:
    """
    Output text information to player. To be displayed in information window in UI
    """
    print(text) #print for now. Will implement a more advanced version when UI is in placec

  def play_round(self, attacker:Character, defender:Character) -> None:
    attack_damage = attacker.attack(opponent_defense=defender.stats.get_defense())
    if attack_damage > 0:
      defender.stats.set_hp(defender.stats.get_hp() - attack_damage)
      self.display_information(f"{defender.get_name()} is taking damage. {defender.stats.get_hp()} HP remaining")
    else:
      self.display_information(f"{defender.get_name()} took no damage. The attack was too weak!")

  def run_game(self) -> None:
    """
    Initiate new game method
    """
    player = self.player
    enemy = self.enemy

    while player.stats.get_hp() > 0 and enemy.stats.get_hp() > 0:
      """
      Player attacks
      """
      self.play_round(attacker=player, defender=enemy)
      if enemy.stats.get_hp() <= 0:
        self.display_information(f"{enemy.get_name()} is knocked out!")
        self.display_information("Game is over! You won")
        break
      """
      Enemy attacks
      """
      self.play_round(attacker=enemy, defender=player)
      if player.stats.get_hp() <= 0:
        self.display_information(f"{player.get_name()} is knocked out!")
        self.display_information("Game is over! You won")
        break
      
#--------------- Trial Run ---------------

warrior_stats = Character_Stats(hp=100, attack=30, defense=5, speed=15)
warrior = Character(name="Baylor", stats=warrior_stats)

goblin_stats = Character_Stats(hp=30, attack=2, defense=2, speed=25) 
goblin = Character(name="Goblus", stats=goblin_stats)

new_game = Game(player=warrior, enemy=goblin)

new_game.run_game()