import Character

class Game:
  """
  Class to define Game attribute and methods
  """
  def __init__(self, player:Character, enemy:Character) -> None:
    self.player = player
    self.enemy = enemy
    pass

  def run_game(self):
    """
    Initiate new game method
    """
    pass

  def fail_state(self):
    """
    Cause game to end upon game loss condition met
    """
    pass

  def win_state(self):
    """
    Cause game to end upon game win condition met
    """
    pass