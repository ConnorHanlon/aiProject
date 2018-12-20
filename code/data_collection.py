import random
import sys
import time
print(sys.path)

sys.path.append('problems')
sys.path.append('algorithms')


from copy import deepcopy
from scheduling import Scheduling
from annealing import SimulatedAnnealing
from beam_search import BeamSearch

class DataCollection:
    def __init__(self):
        self.searches = {
            "SA" : SimulatedAnnealing(
                verbose=False,
                alpha=.98,
                start=500000,
                end=.25,
                iterations=100),
            "Beam" : BeamSearch(
                verbose=False,
                beam_size=1)
            }
        self.file = "final_data.txt"
        self.problem = {
            "scheduling": Scheduling,
        }

    def run_multiple_tests(self, problem, dest_file=None, type_search="SA", duplicates=1):
        for i in range(duplicates):
            copy_problem = deepcopy(problem)
            self.run_test(problem=copy_problem, destination_file=dest_file,  type_search=type_search)

    def run_test(self, problem, destination_file=None, type_search="SA"):
        s = self.searches[type_search]
        try:
            search = s
            prob = deepcopy(problem)
            start_time = time.time()
            search.solve(prob)
            end_time = time.time()
            if not destination_file == None:
                f = open(destination_file, "a+")
            else:
                f = open(prob.file, "a+")
            if search.solution == None:
                if search.time_limit_reached:
                    f.write("Time limit of %d seconds has been reached \n" % search.cutoff_time)
                f.write("No solution found\n")
            else:
                for node in search.solution:
                    f.write("\n%s Search with Neighbor Function: %s, " % (type_search, prob.neighbor_selection))
                    f.write("Number of Jobs: %d, " % prob.job_count)
                    f.write("Number of People: %d \n" % prob.people_count)
                    f.write("State: %s\n" % node.state)
                    if type_search == "Beam":
                        f.write("Beam Size: %d \n" % search.beam_size)
                        f.write("Objective Function Evaluation: %d \n" % prob.apply_objective_function(node.state))
                        f.write("Time to complete search: %s \n" % (end_time-start_time))
                        f.write("Total Node count: %s \n" % search.total_node_count)
                    else:
                        f.write("Objective Function Evaluation: %d \n" % prob.apply_objective_function(node.state))
                        f.write("Time to complete search: %s \n" % (end_time-start_time))
                        f.write("Total Node count (Total iterations): %s \n" % search.total_node_count)
                f.close()
        except:
            f = open(prob.file, "a+")
            f.write("\nCould not handle %s\n" % search.strategy)
            f.close()


    # End_Time for setters are in seconds, default to 1 hour
    def set_SimulatedAnnealing(self, verbose=False,alpha=.98,start=500000,end=.25,iterations=100, end_time=3600):
        self.searches["SA"] = SimulatedAnnealing(verbose, alpha, start, end, iterations, end_time)

    def set_BeamSearch(self, verbose=False, beam=1, end_time=3600):
        self.searches["Beam"] = BeamSearch(verbose=verbose, beam_size=beam, cutoff_time=end_time)
