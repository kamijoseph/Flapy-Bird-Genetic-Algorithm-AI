
import config
import player

class Population:
    def __init__(self, size):
        self.players = []
        self.size = size
        for i in range(0, self.size):
            self.players.append(player.Player())

    def update_live_players(self):
        for player in self.players:
            if player.alive:
                player.look()
                player.think()
                player.draw(config.window)
                player.update(config.ground)
    
    # return true if all players are dead
    def extinct(self):
        extinct = True
        for player in self.players:
            if player.alive:
                extinct = False
        
        return extinct