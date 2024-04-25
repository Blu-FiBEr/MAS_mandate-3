import random
from graph import Graph
from vertex import Vertex
from edge import Edge

class Policy:
    def __init__(self, graph, init_count):
        self.graph = graph
        self.policy = {}  # Dictionary to store policy for each vertex
        self.policy_particles = init_count

        # Initialize policy for each vertex
        for vertex_name in self.graph.vertices.keys():
            self.policy[vertex_name] = {}
            neighbors = self.graph.get_neighbors(Vertex(vertex_name))
            num_neighbors = len(neighbors)
            self.policy[vertex_name]["total"] = num_neighbors * init_count
            if num_neighbors > 0:
                count_per_action = init_count
                for neighbor in neighbors:
                    self.policy[vertex_name][neighbor] = count_per_action
            # else:
            #     # If vertex has no neighbors, assign equal probability to stay in the same vertex
            #     self.policy[vertex_name][vertex_name] = 1
            

    def get_policy(self):
        """
        Get the policy structure.
        """
        return self.policy

    def choose_action(self, vertex, arg_max = 0):
        """
        Choose one of the neighbors of a given vertex using the counts array of the vertex.
        """
        intermediate = list(self.policy[vertex.name].keys())
        intermediate.remove("total")
        neighbors = intermediate
        if(neighbors == None or len(neighbors) == 0) : 
            return None
        # probabilities = list(self.policy[vertex.name].values())
        probabilities = [(self.policy[vertex.name][neighb]/self.policy[vertex.name]["total"]) for neighb in neighbors]
        chosen_neighbor = random.choices(neighbors, probabilities)[0]

        if (arg_max == 1):
            chosen_neighbor = max(neighbors, key=lambda n: self.policy[vertex.name][n] / self.policy[vertex.name]["total"])

        return chosen_neighbor
    
    def update_count(self, vertex_1, vertex_2, prob, delta):
        if(vertex_1.name == vertex_2.name): return

        if(random.random() > prob): return
        
        initial_count = self.policy[vertex_1.name][vertex_2.name]
        
        self.policy[vertex_1.name][vertex_2.name] += delta
        if(self.policy[vertex_1.name][vertex_2.name] < self.policy_particles):
            self.policy[vertex_1.name][vertex_2.name] = self.policy_particles

        self.policy[vertex_1.name]["total"] += self.policy[vertex_1.name][vertex_2.name] - initial_count

        return
