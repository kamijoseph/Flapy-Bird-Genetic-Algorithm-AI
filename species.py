
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
    
    @staticmethod
    def weight_difference(brain_1, brain_2):
        total_weight_difference = 0
        for i in range(0, len(brain_1.connections)):
            for j in range(0, len(brain_2.connections)):
                if i == j:
                    total_weight_difference += abs(
                        brain_1.connections[i].weight - brain_2.connections[j].weight
                    )
                    return total_weight_difference