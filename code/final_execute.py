import sys
import random
sys.path.append('problem')
sys.path.append('algorithms')


from annealing import SimulatedAnnealing
from scheduling import Scheduling
from beam_search import BeamSearch
from data_collection import DataCollection

if __name__ == '__main__':

    dataCollector = DataCollection()

    # Different Problem Sizes:
    # n = [6, 7, 8, 9, 10]
    # p = 4
    # max_time = 5
    # times: random between 0 and max_time
    max_time = 5

    # Problem Size 1:
    # n=6, p=4, times random assignment between 0 and max_time
    # variable neighbor selectors
    n = 6
    p = 4
    times = [random.randint(1,max_time) for i in range(n)]
    problem1_max = Scheduling( job_times = times,
                          people_count = p,
                          neighbor_selection="max",
                          objective_fn="min_max",
                          start_fn="random"
                          )
    problem1_min= Scheduling( job_times = times,
                          people_count = p,
                          neighbor_selection="min",
                          objective_fn="min_max",
                          start_fn="random"
                          )
    problem1_all_comb = Scheduling( job_times = times,
                          people_count = p,
                          neighbor_selection="all_comb",
                          objective_fn="min_max",
                          start_fn="random"
                          )

    # Problem Size 2:
    # n=7, p=4, times random assignment between 0 and max_time
    # variable neighbor selectors
    n = 7
    p = 4
    times = [random.randint(1,max_time) for i in range(n)]
    problem2_max = Scheduling( job_times = times,
                          people_count = p,
                          neighbor_selection="max",
                          objective_fn="min_max",
                          start_fn="random"
                          )
    problem2_min= Scheduling( job_times = times,
                          people_count = p,
                          neighbor_selection="min",
                          objective_fn="min_max",
                          start_fn="random"
                          )
    problem2_all_comb = Scheduling( job_times = times,
                          people_count = p,
                          neighbor_selection="all_comb",
                          objective_fn="min_max",
                          start_fn="random"
                          )

    # Problem Size 3:
    # n=8, p=4, times random assignment between 0 and max_time
    # variable neighbor selectors
    n = 8
    p = 4
    times = [random.randint(1,max_time) for i in range(n)]
    problem3_max = Scheduling( job_times = times,
                          people_count = p,
                          neighbor_selection="max",
                          objective_fn="min_max",
                          start_fn="random"
                          )
    problem3_min= Scheduling( job_times = times,
                          people_count = p,
                          neighbor_selection="min",
                          objective_fn="min_max",
                          start_fn="random"
                          )
    problem3_all_comb = Scheduling( job_times = times,
                          people_count = p,
                          neighbor_selection="all_comb",
                          objective_fn="min_max",
                          start_fn="random"
                          )

    # Problem Size 4:
    # n=9, p=4, times random assignment between 0 and max_time
    # variable neighbor selectors
    n = 9
    p = 4
    times = [random.randint(1,max_time) for i in range(n)]
    problem4_max = Scheduling( job_times = times,
                          people_count = p,
                          neighbor_selection="max",
                          objective_fn="min_max",
                          start_fn="random"
                          )
    problem4_min= Scheduling( job_times = times,
                          people_count = p,
                          neighbor_selection="min",
                          objective_fn="min_max",
                          start_fn="random"
                          )
    problem4_all_comb = Scheduling( job_times = times,
                          people_count = p,
                          neighbor_selection="all_comb",
                          objective_fn="min_max",
                          start_fn="random"
                          )

    # Problem Size 5:
    # n=10, p=4, times random assignment between 0 and max_time
    # variable neighbor selectors
    n = 10
    p = 4
    times = [random.randint(1,max_time) for i in range(n)]
    problem5_max = Scheduling( job_times = times,
                          people_count = p,
                          neighbor_selection="max",
                          objective_fn="min_max",
                          start_fn="random"
                          )
    problem5_min= Scheduling( job_times = times,
                          people_count = p,
                          neighbor_selection="min",
                          objective_fn="min_max",
                          start_fn="random"
                          )
    problem5_all_comb = Scheduling( job_times = times,
                          people_count = p,
                          neighbor_selection="all_comb",
                          objective_fn="min_max",
                          start_fn="random"
                          )



    # Experiment 1: Different Sizes vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    #
    # # Experiment 1-1: problem1_max -> n = 6, p = 4
    # dataCollector.set_BeamSearch(beam=5, end_time=300)
    # dataCollector.set_SimulatedAnnealing(end_time=300)
    # dataCollector.run_multiple_tests(problem1_max, type_search="Beam", duplicates=1)
    # dataCollector.run_multiple_tests(problem1_max, type_search="SA", duplicates=5)
    #
    # # Experiment 1-2: problem2_max -> n = 7, p = 4
    # dataCollector.set_BeamSearch(beam=5, end_time=300)
    # dataCollector.set_SimulatedAnnealing(end_time=300)
    # dataCollector.run_multiple_tests(problem2_max, type_search="Beam", duplicates=1)
    # dataCollector.run_multiple_tests(problem2_max, type_search="SA", duplicates=1)
    #
    #
    # # Experiment 1-3: problem3_max -> n = 8, p = 4
    # dataCollector.set_BeamSearch(beam=5, end_time=300)
    # dataCollector.set_SimulatedAnnealing(end_time=300)
    # dataCollector.run_multiple_tests(problem3_max, type_search="Beam", duplicates=1)
    # dataCollector.run_multiple_tests(problem3_max, type_search="SA", duplicates=1)
    #
    #
    # # Experiment 1-4: problem4_max -> n = 9, p = 4
    # dataCollector.set_BeamSearch(beam=5, end_time=300)
    # dataCollector.set_SimulatedAnnealing(end_time=300)
    # dataCollector.run_multiple_tests(problem4_max, type_search="Beam", duplicates=1)
    # dataCollector.run_multiple_tests(problem4_max, type_search="SA", duplicates=1)
    #
    #
    # # Experiment 1-5: problem5_max -> n = 10, p = 4
    # dataCollector.set_BeamSearch(beam=5, end_time=300)
    # dataCollector.set_SimulatedAnnealing(end_time=300)
    # dataCollector.run_multiple_tests(problem5_max, type_search="Beam", duplicates=1)
    # dataCollector.run_multiple_tests(problem5_max, type_search="SA", duplicates=1)
    #
    #
    # # # Experiment 2: Varied Beam Size
    # # # Problem3_max held constant
    # # # Beam Sizes = [5, 10, 15, 20, 25]
    # # Experiment 2-1: Beam Size = 5
    # dataCollector.set_BeamSearch(beam=5, end_time=10)
    # # dataCollector.set_SimulatedAnnealing(end_time=300)
    # # dataCollector.run_multiple_tests(problem3_max, type_search="Beam", duplicates=5)
    # # dataCollector.run_multiple_tests(problem3_max, type_search="SA", duplicates=1)
    # #
    # # # Experiment 2-2:  Beam Size = 10
    dataCollector.set_BeamSearch(beam=10, end_time=300)
    # # dataCollector.set_SimulatedAnnealing(end_time=300)
    dataCollector.run_test(problem3_max, type_search="Beam")
    dataCollector.set_BeamSearch(beam=10, end_time=300)
    dataCollector.run_test(problem3_max, type_search="Beam")
    # # dataCollector.run_multiple_tests(problem3_max, type_search="SA", duplicates=1)
    # #
    # #
    # # # Experiment 2-3:  Beam Size = 15
    dataCollector.set_BeamSearch(beam=15, end_time=300)
    # # dataCollector.set_SimulatedAnnealing(end_time=300)
    dataCollector.run_multiple_tests(problem3_max, type_search="Beam")
    dataCollector.set_BeamSearch(beam=15, end_time=300)
    dataCollector.run_multiple_tests(problem3_max, type_search="Beam")
    # # dataCollector.run_multiple_tests(problem3_max, type_search="SA", duplicates=5)
    # #
    # #
    # # # Experiment 2-4: Beam Size = 20
    dataCollector.set_BeamSearch(beam=20, end_time=300)
    # # dataCollector.set_SimulatedAnnealing(end_time=300)
    dataCollector.run_multiple_tests(problem3_max, type_search="Beam")
    dataCollector.set_BeamSearch(beam=20, end_time=300)
    dataCollector.run_multiple_tests(problem3_max, type_search="Beam")
    # # dataCollector.run_multiple_tests(problem3_max, type_search="SA", duplicates=5)
    # #
    # #
    # # # Experiment 2-5:  Beam Size = 25
    dataCollector.set_BeamSearch(beam=25, end_time=300)
    # # dataCollector.set_SimulatedAnnealing(end_time=5)
    dataCollector.run_multiple_tests(problem3_max, type_search="Beam")
    dataCollector.set_BeamSearch(beam=25, end_time=300)
    dataCollector.run_multiple_tests(problem3_max, type_search="Beam")
    # # dataCollector.run_multiple_tests(problem3_max, type_search="SA", duplicates=1)
    # #
    # #
    # # # # Experiment 3a: Neighbor Selection MAX
    # # # # Beam Size Constant at 5
    # # # # Size held constant at n=7, p=4
    # dataCollector.set_BeamSearch(beam=5, end_time=300)
    # # dataCollector.set_SimulatedAnnealing(end_time=300)
    # # dataCollector.run_multiple_tests(problem2_max, type_search="Beam", duplicates=1)
    # # dataCollector.run_multiple_tests(problem2_max, type_search="SA", duplicates=1)
    #
    #
    # # # Experiment 3b: Neighbor Selection ALL_COMB
    # # # Beam Size Constant at 5
    # # # Size held constant at n=7, p=4
    # dataCollector.set_BeamSearch(beam=5, end_time=300)
    # # # dataCollector.set_SimulatedAnnealing(end_time=300)
    #
    # # dataCollector.run_multiple_tests(problem2_all_comb, type_search="Beam", duplicates=1)
    # dataCollector.run_test(problem2_all_comb, type_search="Beam")
    # dataCollector.run_test(problem2_all_comb, type_search="Beam")
    # dataCollector.run_test(problem2_all_comb, type_search="Beam")
    # dataCollector.run_test(problem2_all_comb, type_search="Beam")
    # dataCollector.run_multiple_tests(problem2_all_comb, type_search="SA", duplicates=1)


    # Experiment 3b: Neighbor Selection MIN
    # Beam Size Constant at 5
    # Size held constant at n=7, p=4
    # dataCollector.set_BeamSearch(beam=5, end_time=5)
    # dataCollector.run_test(problem2_min, type_search="Beam")
    # dataCollector.set_SimulatedAnnealing(end_time=300)
    # dataCollector.run_test(problem2_min, type_search="SA")
