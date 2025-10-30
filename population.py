
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

        print("KILL EXTINCT")
        self.kill_extinct_species()

        print("SORT BY FITNESS")
        self.sort_species_by_fitness()

        print("CHILDREN FOR NEXT GEN")
        self.next_gen()
    
    def speciate(self):
        for specie in self.species:
            specie.players = []

        for player in self.players:
            add_to_species = False
            for specie in self.species:
                if specie.similarity(player.brain):
                    specie.add_to_species(player)
                    add_to_species = True
                    break
            if not add_to_species:
                self.species.append(species.Species(player))
    
    def calculate_fitness(self):
        for player in self.players:
            player.calculate_fitness()
        for specie in self.species:
            specie.calculate_average_fitness()

    def kill_extinct_species(self):
        species_bin = []
        for specie in self.species:
            if len(specie.players) == 0:
                species_bin.append(specie)
        for specie in species_bin:
            self.species.remove(specie)
    
    def sort_species_by_fitness(self):
        for specie in self.species:
            specie.sort_players_by_fitness()

        self.species.sort(
            key = operator.attrgetter("benchmark_fitness"),
            reverse = True
        )
    
    def next_gen(self):
        children = []

        # cloning champion of each species
        for specie in self.species:
            children.append(specie.champion.clone())

        # filling open player slots with children
        children_per_species = math.floor(
            (self.size - len(self.species)) / len(self.species)
        )
        for specie in self.species:
            for i in range(0, children_per_species):
                children.append(specie.offspring())
        
        while len(children) < self.size:
            children.append(self.species[0].offspring())

        self.players = []
        for child in children:
            self.players.append(child)
        self.generation += 1

    # return true if all players are dead
    def extinct(self):
        extinct = True
        for player in self.players:
            if player.alive:
                extinct = False
        
        return extinct