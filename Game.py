from Character import Character
from Character_Stats import Character_Stats

class Game:
  """
  Class to define Game attribute and methods
  """
  def __init__(self) -> None:
    self.player = None
    self.enemy = None

  def create_characters(self, player_name:str):
      """
      Ask player to create their character and select an enemy
      """
      enemy_name ="Goblin King" # Placeholder name 

      warrior_stats = Character_Stats(hp=100, attack=30, defense=5, speed=15) # Placeholder stats
      warrior = Character(name=player_name, stats=warrior_stats)

      enemy_stats = Character_Stats(hp=30, attack=2, defense=2, speed=25) # Placeholder stats
      enemy = Character(name=enemy_name, stats=enemy_stats)
      
      self.player = warrior
      self.enemy = enemy 