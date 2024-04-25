from graph import Graph
from mas import MAS
from policy import Policy
import matplotlib.pyplot as plt
import numpy as np


NUM_VERTICES = 1000
NUM_EDGES = 6000
MAX_WEIGHT = 10
NUM_AGENTS = 1
POLICY_PARTICLES = 20
MAX_LEN = NUM_VERTICES
NUM_EPISODES = 5


main_graph = Graph(NUM_VERTICES, NUM_EDGES, MAX_WEIGHT)

# main_policy = Policy(main_graph, POLICY_PARTICLES)
# main_mas = MAS(main_graph, NUM_AGENTS, main_policy)


# train(5)


# diffs, num_diffs, avg_loss, test_distances = main_mas.test_policy(MAX_LEN)

# print("Differences:", diffs)
# print("Number of differences:", num_diffs)
# print("Avg_loss:", avg_loss)
# print("Goal: " + main_graph.goal_vertex.name)
# print(test_distances)


def lesse():
    for i in range(1, 50):
        avg_avg = 0
        for j in range(0, 10):
            main_policy = Policy(main_graph, POLICY_PARTICLES)

            main_mas = MAS(main_graph, i, main_policy)
            for _ in range(0, (int)(200/i)):
                main_mas.run_agents(MAX_LEN, NUM_EPISODES)

            diffs, num_diffs, avg_loss, test_distances = main_mas.test_policy(
                MAX_LEN)

            # print("Differences:", diffs)
            # print("Number of differences:", num_diffs)
            # print("Avg_loss:", avg_loss)
            avg_avg += avg_loss
        # print("Goal: " + main_graph.goal_vertex.name)
        # print(test_distances)
        print(avg_avg/10)

# lesse()


def LossAgentsPlot():
    losses = []
    for num_agents in range(1, 100):
        total_loss = [0,0]
        for _ in range(5):
            main_policy = Policy(main_graph, POLICY_PARTICLES)

            main_mas = MAS(main_graph, num_agents, main_policy)
            main_mas.train(1, MAX_LEN, NUM_EPISODES)
            _, _, loss, _ = main_mas.test_policy(MAX_LEN)
            if(loss != 0): 
                total_loss = [total_loss[0] + loss, total_loss[1] + 1]
                print(loss)
        
        avg_loss = total_loss[0]/total_loss[1]
        print("avg_loss : " + str(avg_loss))
        losses.append(avg_loss)
    plt.plot(losses)
    plt.savefig('plot.png')
    plt.close()
    return


# LossAgentsPlot()

def LossEpochsPlots():
    num_agent_performance = {}
    # for num_agents in list(np.linspace(1, 100, 10, dtype = int)):
    for num_agents in [ 2, 7,  23, 67]:
        main_policy = Policy(main_graph, POLICY_PARTICLES)
        main_mas = MAS(main_graph, num_agents, main_policy)
        num_agent_performance[str(num_agents)] = []
        for _ in range(25):
            main_mas.run_agents(MAX_LEN, NUM_EPISODES)
            _, _, loss, _ = main_mas.test_policy(MAX_LEN)
            print(str(num_agents) + " : " + str(loss))
            num_agent_performance[str(num_agents)].append(loss)

    num_agent_performance["2"][0] = num_agent_performance["2"][1]
    for key, value in num_agent_performance.items():
        plt.plot(value, label=key)
    plt.tight_layout()
    plt.legend()
    plt.savefig("second_plot.png")

LossEpochsPlots()   

# print(main_mas.policy.policy)

# def find_differences(dict1, dict2):
#     differences = {}
#     num_differences = 0

#     # Check keys in dict1
#     for key in dict1:
#         if key not in dict2:
#             differences[key] = (dict1[key], None)
#             num_differences += 1
#         elif dict1[key] != dict2[key]:
#             differences[key] = (dict1[key], dict2[key])
#             num_differences += 1

#     # Check keys in dict2 not in dict1
#     for key in dict2:
#         if key not in dict1:
#             differences[key] = (None, dict2[key])
#             num_differences += 1

#     return differences, num_differences


# # print(main_graph.vertices)

# dict1 = main_mas.test_policy(MAX_LEN)
# dict2 = main_graph.dijkstra_distances
# # print(dict2)

# diffs, num_diffs = find_differences(dict1, dict2)
