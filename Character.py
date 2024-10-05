from Character_Stats import Character_Stats

class Character:
  """
  Class to define character attributes and methods
  """
  def __init__(self, name: str, stats: Character_Stats) -> None:
    self.__name = name
    self.stats = stats
  
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