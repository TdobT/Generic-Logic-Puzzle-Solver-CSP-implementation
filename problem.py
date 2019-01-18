from constraint_hypergraph import ConstraintsHyperGraph


class CostraintSatisfactionProblem():

    def __init__(self):
        self.problem_variables = dict()
        self.contraint_hypergraph = ConstraintsHyperGraph(self.problem_variables)


    def add_variable(self, variable_name, variable_domain):
        self.problem_variables[variable_name] = variable_domain
        self.contraint_hypergraph.add_node(variable_name, variable_domain)


    def add_variables(self, variables_names, variables_domain):
        for var_name in variables_names:
            self.problem_variables[var_name] = variables_domain


    def add_constraint(self, constraint_scope, constraint_relation):

        for var_name in constraint_scope:
            if not self.problem_variables[var_name]:
                raise ValueError("All variables used must be already been defined")

        self.contraint_hypergraph.add_hyper_edge(constraint_scope, constraint_relation)

    def solve(self):
        pass
