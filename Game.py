from Character import Character
from Character_Stats import Character_Stats

class Game:
  """
  Class to define Game attribute and methods
  """
  def __init__(self) -> None:
    self.player = None
    self.enemy = None
    self.game_active = False
    self.player_active = False
    self.round_count = 0
    self.results = ""
    self.player_moved = False
    self.enemy_moved = False

  def create_characters(self, player_name:str) -> None:
      """
      Ask player to create their character and select an enemy
      """
      enemy_name ="Goblin King" # Placeholder name 

      warrior_stats = Character_Stats(hp=100, attack=30, defense=5, speed=15) # Placeholder stats
      warrior = Character(name=player_name, stats=warrior_stats, is_player=True)

      enemy_stats = Character_Stats(hp=150, attack=25, defense=2, speed=10) # Placeholder stats
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