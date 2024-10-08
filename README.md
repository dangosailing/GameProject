# GameProject
A simple turn-based RPG project written in Python

## About
A turn-based battle RPG where you fight various monsters.
For the initial scope the game will feature one class (Warrior) and one enemy (Goblin).
The game will be rendered using the Tkinter python library.

# Game Flow
Initial turn decided based on which character has the highest speed stat.
Character can chose between attacking and defending. When enemy or player HP hits zero the game ends.

## Stats
HP: hit points. The character health pool. When PC (player character) HP hits zero the game should trigger a fail state, conversley when the enemy NPC (non-player character) HP hits zero the player wins
Attack: base damage value. Subtract the defense value of oppenent and then subtract from HP to get damage
Defense: subtracts from enemy attack to determine damage to HP
Speed: determines who goes first 

## Misc
### Future implementations
Once MVP (minimum viable product) is achieved the following features will be considrerd:
- Status effects
- Skills (move attack and defend into skills)
- Turn duration
- New classes
- New monsters
- Difficulty levels (number of monsters to fight)
- Maybe list version updates here once MVP is reached?

## Setting up virtual env (macOS)
1) python3 -m venv .venv
2) source .venv/bin/activate
3) (To exit virtual environment) deactivate

# App Flow
1) Create character. Just name for now (default to warrior)
2) Battle starts - List encounter flavor text in info_display
3) Determine who moves first
4) If enemy goes first it will attack, if player goes first they can either attack or defend
5) Defend halves the incoming damage from the opponent attack (halved from total damage output)
6) Keep battle going until either player or enemy HP hits zero -> display battle outcome
7) Ask player if they want to save the results. Results include timestamp, outcome, player and enemy name
