# Beam Search and Simulated Annealing as Applied to Job scheduling
-----
## Research Paper and Results of Comparison

The paper is located in the paper directory, and is entitled "FinalPaper.pdf".

-----
## File List and Descriptions
* #### algorithm.py

  * File Origin: Professor Larson and TAs of 4511
  * File Contributor: Connor Hanlon
    * Additions: is_cutoff_time(), current_time(), start_search_timer()

 Base algorithm class implemented by annealing.py and beam_search.py which keeps track of basic information such as node count, current problem, solution, and basic timer functions.

* #### annealing.py

  * File Origin: Professor Larson and TAs of 4511
  * File Contributor: Connor Hanlon
    * Additions: elapsed_time calculation, get_best

  Implementation of the Simulated Annealing search algorithm. The algorithm works by generating a successor(neighbor) of the current node, evaluating the current node and successor's state, and using a temperature function to determine whether to move the search to the successor or continue with the current node. The temperature function allows for "bad" moves to nodes with states worse than the current node, but as the search progresses the amount of moves to worse states decreases.

* #### beam_search.py

  * File Origin: Connor Hanlon

  Implementation of Beam Search algorithm. Creates a beam of size beam_size, then for each node in the beam examines very neighbor and selects the best based on the neighbor selector from scheduling.py. If a neighbor is better, it is added to the beam, otherwise beam removes node and shrinks by one. Continues until objective function evaluates to 0 or beam is empty, after which the best state found through the course of the search is returned as the best.

* #### node.py

  * File Origin: Professor Larson and TAs of 4511
  * File Contributor: Connor Hanlon
    * Additions: make_multiple_nodes()

  Two classes are implemented within node.py. The first is a node factory and the second is a node. Nodes keep track of up to date information on a state, its value, and other relevant information to the state of a search.

* #### problem.py

  * File Origin: Professor Larson and TAs of 4511

  Basic implementation of a problem, used by scheduling.py

* #### scheduling.py

  * File Origin: Professor Larson and TAs of 4511
  * File Contributor: Connor Hanlon
    * Additions: get_all_indices(), get_random_index(), get_person_time_list(), get_person_mintime_list(), find_min_max_people(), get_all_comb_neighbors(), get_max_neighbors(), get_min_neighbors(), get_min_max_neighbors(), get_best(), get_k_best(), job_time(),
    max_objective_function(), min_objective_function(), min_max_objective_function()

    Scheduling problem where people are assigned jobs, and each job has a certain amount of time to complete. This is an optimization problem to get the lowest time amongst all people.

* #### data_collection.py

  * File Origin: Connor Hanlon

  This class allows for easy test running and data acquisition. One test can be run for Beam Search or Simulated Annealing, or multiple tests can be run with the proper inputs. In order to set the specific algorithms in DataCollection, use setters before running tests.

* #### final_execute.py

  * File Origin: Connor Hanlon

  Location of experiment trials.
----
## Data Files

* #### beam_data.txt

  * File Origin: Connor Hanlon

  Generated with DataCollector from final_execute.py, lists the results of all experiments conducted with Beam Search.

* #### sa_data.txt

  * File Origin: Connor Hanlon

  Generated with DataCollector from final_execute.py, lists the results of all experiments conducted with Simulated Annealing.
