import sort_by_X
import sort_by_Y
import next_nearest
import brute_force
import three_opt_swap
import two_opt_swap
import pprint
import tsp_functions
import Genetic_Algorithm
import anneal
import visualize_tsp
end_distances = {"sort by x":0,"sort by y":0,"two opt swap":0,"three opt swap":0,"next nearest":0,"brute force":0,"ga":0,"sa":0}
num_trials = 10
for i in range(num_trials):
    #Test comment
    distances = {"sort by x":0,"sort by y":0,"next nearest":0,"two opt swap":0,"three opt swap":0,"brute force":0,"ga":0,"sa":0}
    coords = tsp_functions.generate_points(200,400)
    distances["sort by y"] = sort_by_Y.sort_by_y(coords)
    distances["sort by x"] = sort_by_X.sort_by_x(coords)
    distances["two opt swap"] = two_opt_swap.twoOptSwap(coords)
    distances["three opt swap"] = three_opt_swap.threeOptSwap(coords)
    distances["next nearest"] = next_nearest.greedy_algo(coords)
    distances["sa"] = anneal.SimAnneal(coords).Anneal()
    distances["ga"] = Genetic_Algorithm.GA(coords)
    print("Trial " + str(i) + ":")
    pprint.pprint(distances)
    end_distances["sort by y"] = end_distances["sort by y"]
    end_distances["sort by y"] = end_distances["sort by y"]
    end_distances["sort by x"] = end_distances["sort by y"]
    end_distances["two opt swap"] = end_distances["sort by y"]
    end_distances["three opt swap"] = end_distances["sort by y"]
    end_distances["next nearest"] = end_distances["sort by y"]
    end_distances["sa"] = end_distances["sort by y"]
    end_distances["ga"] = end_distances["sort by y"]
for i in end_distances:
    end_distances[i] /= num_trials
print("The end distances are:")
pprint.pprint(end_distances)
