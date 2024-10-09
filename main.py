from Game import Game
from Game_UI import Game_UI

class Main(Game, Game_UI):
    """
    Class used to bind the game and the ui together
    """
    def __init__(self):
        Game.__init__(self) # Multiple inheritance requires referencing each class instead of relying on super
        Game_UI.__init__(self)
    
    def configure_button_methods(self):
        super()
        self.button_new_game.config(command = lambda: self.update_info_window("NEW GAME"))
        self.button_quit.config(command = exit)
        self.button_new_round.config(command = lambda: self.update_info_window("NEW ROUND"))
        self.button_attack.config(command = lambda: self.update_info_window("ATTACK"))
        
    def initialize_game(self):
        self.render_game_frame()
        self.create_widgets()
        self.configure_button_methods()
        self.place_widgets_game()
        self.root.mainloop()

new_game = Main()
new_game.initialize_game()

