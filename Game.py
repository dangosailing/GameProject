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
    player = self.player
    enemy = self.enemy

    while player.stats.get_hp() > 0 and enemy.stats.get_hp() > 0:
      """
      Player attacks
      """
      player_attack_damage = player.attack(opponent_defense=enemy.stats.get_defense())
      if player_attack_damage > 0:
        enemy.stats.set_hp(enemy.stats.get_hp() - player_attack_damage)
        print(f"{enemy.get_name()} is taking damage. {enemy.stats.get_hp()} HP remaining")
      else:
        print(f"{enemy.get_name()} took no damage. The attack was too weak!")
      if enemy.stats.get_hp() <= 0:
        print(f"{enemy.get_name()} is knocked out!")
        print("Game is over! You won")
        break
      """
      Enemy attacks
      """
      enemy_attack_damage = enemy.attack(opponent_defense=player.stats.get_defense())
      if enemy_attack_damage > 0:
        player.stats.set_hp(player.stats.get_hp() - enemy_attack_damage)
        print(f"{player.get_name()} is taking damage. {player.stats.get_hp()} HP remaining")
      else:
        print(f"{player.get_name()} took no damage. The attack was too weak!")
      if player.stats.get_hp() <= 0:
        print(f"{player.get_name()} is knocked out!")
        print("Game is over! You won")
        break
      
#--------------- Trial Run ---------------

warrior_stats = Character_Stats(hp=100, attack=30, defense=5, speed=15)
warrior = Character(name="Baylor", stats=warrior_stats)

goblin_stats = Character_Stats(hp=30, attack=2, defense=2, speed=25) 
goblin = Character(name="Goblus", stats=goblin_stats)

new_game = Game(player=warrior, enemy=goblin)

new_game.run_game()