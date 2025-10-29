
# species
import random
import operator

class Species:
    def __init__(self, player):
        self.players = []
        self.average_fitness = 0
        self.threshold = 1.2
        self.players.append(player)
        self.benchmark_fitness = player.fitness
        self.benchmark_brain = player.brain.clone()
        self.champion = player.clone()

    def similarity(self, brain):
        similarity =  self.weight_difference(self.benchmark_brain, brain)
        return self.threshold > similarity