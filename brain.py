
# the neural network
import node
import connection
import random

class Brain:
    def __init__(self, inputs):
        self.connections = []
        self.nodes = []
        self.inputs = inputs
        self.net = []
        self.layers = 2

        # input nodes
        for i in range(0, self.inputs):
            self.nodes.append(node.Node(i))
            self.nodes[i].layer = 0

        # bias node
        self.nodes.append(node.Node(3))
        self.nodes[3].layer = 0
        
        # output node
        self.nodes.append(node.Node(4))
        self.nodes[4].layer = 1

        # connections
        for i in range(0, 4):
            self.connections.append(connection.Connection(
                self.nodes[i], self.nodes[4], random.uniform(-1, 1)
            ))

    def connect_nodes(self):
        for i in range(0, len(self.nodes)):
            self.nodes[i].connections = []
        
        for i in range(0, len(self.connections)):
            self.connections[i].from_node.connections.append(self.connections[i])

    def generate_network(self):
        pass