from Character import Character
from Character_Stats import Character_Stats

class Game:
  """
  Class to define Game attribute and methods
  """
  def __init__(self, player:Character, enemy:Character) -> None:
    self.player = player
    self.enemy = enemy

  def run_game(self):
    """
    Initiate new game method
    """
    while self.player.stats.get_hp() > 0 and self.enemy.stats.get_hp() > 0:
      """
      Player attacks
      """
      enemy_hp = self.enemy.stats.get_hp() + self.enemy.stats.get_defense() - self.player.stats.get_attack()
      if enemy_hp < self.enemy.stats.get_hp(): # To prevent enemy HP from growing if defense is greater than attack and the resulting HP is bigger than before the attack 
        self.enemy.stats.set_hp(enemy_hp)
        print(f"{self.enemy.get_name()} is taking damage, {self.enemy.stats.get_hp()} HP remaining")
      else:
        print(f"{self.enemy.get_name()} took no damage. The attack was too weak!")
      if self.enemy.stats.get_hp() <= 0:
        print(f"{self.enemy.get_name()} is knocked out!")
        print("Game is over! You won")
        break
      """
      Enemy attacks
      """
      player_hp = self.player.stats.get_hp() + self.player.stats.get_defense() - self.enemy.stats.get_attack()
      if player_hp < self.player.stats.get_hp(): # To prevent player HP from growing if defense is greater than attack and the resulting HP is bigger than before the attack 
        self.player.stats.set_hp(player_hp)
        print(f"{self.player.get_name()} is taking damage, {self.player.stats.get_hp()} HP remaining")
      else:
        print(f"{self.player.get_name()} took no damage. The attack was too weak!")
      if self.player.stats.get_hp() <= 0:
        print(f"{self.player.get_name()} is knocked out!")
        print("Game is over! You lost")
        break
      
#--------------- Trial Run ---------------

warrior_stats = Character_Stats(hp=100, attack=30, defense=5, speed=15)
warrior = Character(name="Baylor", stats=warrior_stats)

goblin_stats = Character_Stats(hp=30, attack=2, defense=2, speed=25) 
goblin = Character(name="Goblus", stats=goblin_stats)

new_game = Game(player=warrior, enemy=goblin)

new_game.run_game()