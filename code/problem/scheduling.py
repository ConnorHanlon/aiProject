import random
import operator
import itertools

from problem import Problem
from copy import deepcopy


class Scheduling(Problem):
    '''
    The scheduling problem is an optimization problem that is attempting to minimize
    the time it takes to complete a collection of jobs distributed across a number of
    people or processors or robots or whatever is doing the work. Formally, it would be
    defined as:
    - A collection of _n_ jobs.
    - Each job _j_ take time <i>t<sub>j</sub></i>
    - There are _p_ people to process the jobs
    - Each person completes his/her last job at time <i>p<sub>t</sub></i>
    - The time to complete all jobs is the maximum over all <i>p<sub>t</sub></i>

    -job_times is list of times for each job

    So there are two lists: one list describes amount of time to do a job
    the other assings a person to a job. So lets say there are 3 people and 10 jobs,
    an initial state can be

    [0, 0, 2, 1, 2, 0, 1, 1, 1, 2]
    with times for jobs
    [5, 3, 3, 6, 8, 2, 6, 3, 8, 1]

    So the amount of time it takes person1(0 in job list) to finish is:
    p1 = 5+3+2      = 10
    p2 = 6+6+3+8    = 23
    p3 = 3+8+1      = 12
    '''

    def __init__(self, job_times, people_count = 3, start_state=None,
                 neighbor_selection="max", objective_fn="max_obj_fn", start_fn="random"):
        Problem.__init__(self, [])
        self.job_count = len(job_times)
        self.job_times = job_times
        self.people_count = people_count
        self.start_state = start_state
        self.person_time_dict = {}
        self.file = "sa_data.txt"

        self.start_fn = start_fn
        # Keeping these in case you want to experiment with objective fn and neighbors
        self.neighbor_selection = neighbor_selection
        self.objective_fn = objective_fn
        self.initialize_neighbor_selection_dict()
        self.initialize_objective_fn_dict()

    def reset(self):
        self.start_state = None

    def get_all_indices(self, state, person):
        index_list = []
        iter = 0
        while iter < self.job_count:
            if state[iter] == person:
                index_list.append(iter)
            iter += 1
        return index_list

    def get_random_index(self, state, person):
        index_list = []
        iter = 0
        while iter < self.job_count:
            if state[iter] == person:
                index_list.append(iter)
            iter += 1
        length = len(index_list)
        random_index = random.randint(0, length-1)
        return index_list[random_index]

    # error: if person count more than actual people assigned, then person_time list incorrect.
    def get_person_time_list(self, state):
        person_time_list = [0 for i in range(self.people_count)]
        copy_state = deepcopy(state)
        iter = 0
        while iter < self.job_count:
            person = copy_state[iter]
            time_job = self.job_times[iter]
            old_time = person_time_list[person]
            new_time = old_time + time_job
            person_time_list[person] = new_time
            iter += 1
        return person_time_list

    # initialize person_time_list to more than max possible time, this makes a possible unassigned person redundant
    # call with get_min_people
    def get_person_mintime_list(self, state):
        max_time = sum(self.job_times) + 1
        person_time_list = [max_time for i in range(self.people_count)]
        copy_state = deepcopy(state)
        iter = 0
        while iter < self.job_count:
            person = copy_state[iter]
            time_job = self.job_times[iter]
            old_time = person_time_list[person]
            if old_time == max_time:
                old_time = 0
            new_time = old_time + time_job
            person_time_list[person] = new_time
            iter += 1
        return person_time_list

    # returns tuple of person with max time and min time
    def find_min_max_people(self, state):
        person_time_list = self.get_person_time_list(state)
        max_person = person_time_list.index(max(person_time_list))
        person_mintime_list = self.get_person_mintime_list(state)
        min_person = person_mintime_list.index(min(person_mintime_list))
        return (max_person, min_person)

# vvvvvvvvvvvvvvvvv Neighbor Selection Functions vvvvvvvvvvvvvvvvvvvvvvvvv

    def select_neighbors(self, state):
        copy_state = deepcopy(state)
        return self.selection_for_neighbor[self.neighbor_selection](copy_state)

    def get_all_comb_neighbors(self, state):
        copy_state = deepcopy(state)
        neighbors = []
        for person in range(0, self.people_count):
            neighbors.append([person])
        notDone = True
        while notDone:
            partial_neighbor = []
            for n in neighbors:
                for p in range(0, self.people_count):
                    temp_n = list(n)
                    if len(n) < len(copy_state):
                        temp_n.append(p)
                        partial_neighbor.append(temp_n)
            if partial_neighbor == []:
                notDone = False
            else:
                neighbors = partial_neighbor
        neighbors.remove(copy_state)
        return neighbors


    # for the person with the most time, using the index of a job that is assigned
    # to that person, go through every other person that can be assigned in that
    # person's place. Each person added ends in a new neighbor state, this the total
    # amount of neighbors returned is the # of people.
    def get_max_neighbors(self, state):
        neighbors = []
        peep = self.find_min_max_people(state)
        max_peep = peep[0]
        indices = self.get_all_indices(state, max_peep)
        # index_max = self.get_random_index(state, max_peep)
        for index in indices:
            for person in range(0, self.people_count):
                if not person == max_peep:
                    neighbor_state = deepcopy(state)
                    # neighbor_state[index_max] = person
                    neighbor_state[index] = person
                    neighbors.append(neighbor_state)
        return neighbors

    # for the person with the least time, using the index of a job that is assigned
    # to that person, go through every other person that can be assigned in that
    # person's place. Each person added ends in a new neighbor state, this the total
    # amount of neighbors returned is the # of people.
    def get_min_neighbors(self, state):
        neighbors = []
        peep = self.find_min_max_people(state)
        min_peep = peep[1]
        indices = self.get_all_indices(state, min_peep)
        for index in indices:
            for person in range(0, self.people_count):
                if not person == min_peep:
                    neighbor_state = deepcopy(state)
                    neighbor_state[index] = person
                    neighbors.append(neighbor_state)
        return neighbors


    # combines get min and get max, returns a list size of 2*self.people_count - 2
    def get_min_max_neighbors(self, state):
        neighbors = self.get_max_neighbors(state)
        neighbors.extend(self.get_min_neighbors(state))
        return neighbors

# ^^^^^^^^^^^^^^^^^^ Neighbor Selection Functions ^^^^^^^^^^^^^^^^^^^^^^^^^

    # set initial best successor to first state. evaluate every state
    #  based on the evaluation function and return the best state
    def get_best(self, states):
        best = deepcopy([states[0]])
        best_value = self.apply_objective_function(best[0])
        for s in states:
            s_value = self.apply_objective_function(s)
            if s_value < best_value:
                best = deepcopy([s])
                best_value = s_value
            # map(lambda x: x if self.apply_objective_function(x) < s_value else s, best)
        return best

    def get_k_best(self, states, k):
        k_best = []
        iter = 0
        copy_states = deepcopy(states)
        while iter < k and len(copy_states) > 0:
            best = self.get_best(copy_states)
            k_best.append(best[0])
            copy_states.remove(best[0])
            iter += 1
        return k_best

    def get_random_state(self, states):
        copy_states = deepcopy(states)
        return copy_states[random.randint(0, len(states)-1)]

    def random_solution_state(self):
        # Randomly assign every job to a person
        return [random.randint(0,self.people_count-1) for i in range(self.job_count)]

    def get_initial_state(self):
        if not self.start_fn == "given":
            return self.random_solution_state()
        else:
            return self.start_state

    def job_time(self, jobs):
        total_time = 0
        for job in jobs:
            total_time += self.job_times[job]
        return total_time

# vvvvvvvvvvvvvvvvv Objective Functions vvvvvvvvvvvvvvvvv

    def apply_objective_function(self, state):
        return self.functions_for_evaluation[self.objective_fn](state)

    # if state none, set objective_fn to largest possible time (1 person do all)
    #Gets max time it takes for a person to do a job
    def max_objective_function(self, state):
        person_time_list = self.get_person_time_list(state)
        return max(person_time_list)

    def min_objective_function(self, state):
        person_time_list = self.get_person_mintime_list(state)
        return max(person_time_list)

    def min_max_objective_function(self, state):
        person_time_list = self.get_person_time_list(state)
        max_time = max(person_time_list)
        # person_mintime_list = self.get_person_mintime_list(state)
        min_time = min(person_time_list)
        return (max_time-min_time)

# ^^^^^^^^^^^^^^^^ Objective Functions ^^^^^^^^^^^^^^^^^^^^

    def initialize_neighbor_selection_dict(self):
        self.selection_for_neighbor = {
            # "swap": self.get_neighbor_swap,
            "max" : self.get_max_neighbors,
            "min" : self.get_min_neighbors,
            "both": self.get_min_max_neighbors,
            "all_comb": self.get_all_comb_neighbors
        }

    def initialize_objective_fn_dict(self):
        self.functions_for_evaluation = {
            "max_obj_fn": self.max_objective_function,
            "min_obj_fn": self.min_objective_function,
            "min_max": self.min_max_objective_function
        }

    def pretty_print(self, node):
        job_assignment = node.state
        print("Job Times: ", self.job_times, "\n")
        for p in range(self.people_count):
            jobs = [i for i in range(self.job_count) if job_assignment[i]==p]
            print(p,'has jobs', jobs, " with an evaluation ", self.job_time(jobs))
            # print(jobs, end=" ")
            # print(" with an evaluation of ", self.job_time(jobs))



def all_unique(elements):
    try:
        answer = len(set(elements)) == len(elements)
    except:
        print('FAIL ',elements)
        return True
    return answer
