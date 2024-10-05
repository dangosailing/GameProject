from Character_Stats import Character_Stats

class Character:
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