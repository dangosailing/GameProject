from Character_Stats import Character_Stats
from random import randint
class Character:
  """
  Class to define character attributes and methods
  """
  def __init__(self, name: str, stats: Character_Stats, is_player:bool) -> None:
    self.__name = name
    self.stats = stats
    self.is_player = is_player
    self.stun_duration = 0
    self.unallocated_stat_pts = 50
  
  def get_name(self) -> str:
    """
    name getter method
    """
    return self.__name
  
  def set_name(self) -> None:
    """
    name setter method
    """
    return self.__name
  
  def attack(self, opponent_defense:int) -> int:
    """
    Return damage done to enemy. If enemy defense is higher than attack return 0
    """
    attack_damage = 0
    if self.stats.get_attack() > opponent_defense:
      attack_damage = self.stats.get_attack() - opponent_defense
    return attack_damage
  
  def strong_attack(self) -> int:
    """
    Return damage done to enemy. Attack that can either miss or yield 3 times the damage. Igonres enemy defense.
    """
    attack_modifier = randint(0,3)
    modified_attack_damage = self.stats.get_attack() * attack_modifier
    self.stun_duration = 3 # If player applies a strong attack they become inactive for 2 turns due to exhaustion
    return modified_attack_damage
      
  def did_attack_hit(self, enemy_agility:int) -> bool:
      """
      Use enemy agility as modifier to determine if attack is a hit or miss
      """
      agility_modifier = 100 - enemy_agility
      return randint(0,100) < agility_modifier
