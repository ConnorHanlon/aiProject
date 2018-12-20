from time import monotonic as timer
class Algorithm:
    def __init__(self, verbose=False, cutoff_time=3600):
        self.verbose = verbose
        self.total_node_count = -1
        self.max_frontier_node_count = -1
        self.max_depth = -1
        self.solution = []
        self.problem = None
        self.search_start_time = 0
        self.cutoff_time = cutoff_time
        self.time_limit_reached = False

    def solve(self, problem, all_solutions=False):
        self.reset()
        self.problem = problem

    def reset(self):
        self.total_node_count = -1
        self.max_frontier_node_count = -1
        self.solution = []
        self.max_depth = -1
        self.problem = None
        self.search_start_time = 0
        self.time_limit_reached = False

    def is_cutoff_time(self):
        end_search_time = timer()
        elapsed = end_search_time - self.start_search_time
        return (elapsed > self.cutoff_time)

    def current_time(self):
        current = timer()
        return current-self.start_search_time

    def start_search_timer(self):
        self.start_search_time = 0
        self.start_search_time = timer()


    def print_solution(self):
        if not self.solution:
            print("No solution found.")
            return
        for node in self.solution:
            print('state: ', node.state)
            self.problem.pretty_print(node)
            print("\nObjective function evaluation: ", self.problem.apply_objective_function(node.state))


    def print_stats(self):
        print("Total node count: ", self.total_node_count)
        print("Max frontier count: ", self.max_frontier_node_count)
        print("Max depth of tree: ", self.max_depth)
