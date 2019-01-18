

class ConstraintsHyperGraph():

    def __init__(self, nodes):
        self.nodes = nodes
        self.hyper_edges = []


    def add_hyper_edge(self, nodes, constraint_lambda):
        self.hyper_edges.append((nodes, constraint_lambda))
