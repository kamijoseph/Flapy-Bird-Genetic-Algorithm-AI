
import config
import player
import operator
import math
import species

class Population:
    def __init__(self, size):
        self.players = []
        self.generation = 1
        self.species = []
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
    
    def natural_selection(self):
        print("SPECIATE")
        self.speciate()

        print("CALCULATE FITNESS")
        self.calculate_fitness()

        print("SORT BY FITNESS")
        self.sort_species_by_fitness()

        print("CHILDREN FOR NEXT GEN")
        self.next_gen()
    
    # return true if all players are dead
    def extinct(self):
        extinct = True
        for player in self.players:
            if player.alive:
                extinct = False
        
        return extinct