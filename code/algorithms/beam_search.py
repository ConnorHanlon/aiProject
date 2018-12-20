# Copyright (c) 2018 Connor Hanlon

from copy import deepcopy
from node import Node, NodeFactory
from algorithm import Algorithm

class BeamSearch(Algorithm):
    def __init__(self, verbose=False, beam_size=5, cutoff_time=3600):
        Algorithm.__init__(self, verbose, cutoff_time)
        self.solution = []
        self.beam_size = beam_size
        self.strategy = "Beam Search"

    def reset(self):
        self.solution = []


    def solve(self, problem):
        self.reset()
        self.problem = problem
        beam = []
        succ = []
        last_nodes = []

        node_factory = NodeFactory(verbose = self.verbose)
        initial_node = node_factory.make_node(problem.get_initial_state())
        initial_node.value = problem.apply_objective_function(initial_node.state)

        self.solution = [initial_node]

        if initial_node.value == 0:
            self.total_node_count = 1
            return self.solution

        # neighbor_states = problem.selection_for_neighbor[self.neighbor_selection](initial_node.state)
        neighbor_states = problem.select_neighbors(initial_node.state)
        succ_states = problem.get_k_best(neighbor_states, self.beam_size)
        beam = node_factory.make_multiple_nodes(succ_states)
        # for node in beam:
        #     node.value = problem.apply_objective_function(node.state)
        # self.total_node_count += len(beam)
        self.start_search_timer()
        while not beam == []:
            if self.is_cutoff_time():
                self.time_limit_reached = True
                self.total_node_count = node_factory.node_count
                return self.solution
            for node in beam:
                current_node = deepcopy(node)
                current_node.value = problem.apply_objective_function(current_node.state)
                # nbr_states = problem.selection_for_neighbor[self.neighbor_selection](node.state)
                nbr_states = problem.select_neighbors(current_node.state)
                best_succ_state = problem.get_best(nbr_states)[0]
                best_successor = node_factory.make_node(best_succ_state)
                best_successor.value = problem.apply_objective_function(best_successor.state)
                if best_successor.value == 0:
                    self.solution = [best_successor]
                    self.total_node_count = node_factory.node_count
                    return self.solution
                elif best_successor.value <= current_node.value:
                    succ.append(deepcopy(best_successor))
                else:
                    last_nodes.append(current_node)
            beam = deepcopy(succ)
            succ = []
        # print("state started all same", initial_node.state)
        # self.total_node_count = node_factory.node_count
        best_solution = initial_node
        for nodes in last_nodes:
            if node.value < best_solution.value:
                best_solution = node
        self.solution = [best_solution]
        self.total_node_count = node_factory.node_count
        return self.solution


    def print_stats(self):
        print("Total Nodes: ", self.total_node_count)
        print("Beam Size: ", self.beam_size)
