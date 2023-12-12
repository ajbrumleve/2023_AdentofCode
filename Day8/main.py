import math
import time


def parse_file(file, part):
    map_dict = {}
    with open(file, 'r') as f:
        for line in f:
            if "=" not in line and line != "\n":
                turn_order = line.strip()
            elif "=" in line:
                node = line.split("=")[0].strip()
                turns = line.split("=")[1].strip()[1:-1].split(",")
                map_dict[node] = (turns[0].strip(), turns[1].strip())
    return turn_order, map_dict


def make_move(cur_node, turn, move_dict):
    if turn == "L":
        return move_dict[cur_node][0]
    elif turn == "R":
        return move_dict[cur_node][1]


def process_first_run(tar, map_dict, turns):
    full_run_map = {}
    for key in map_dict.keys():
        cur_node = key
        turn_queue = list(turns)
        while len(turn_queue) > 0:
            next_node = make_move(cur_node, turn_queue.pop(0), map_dict)
            if next_node == tar:
                cur_node = len(turns) - len(turn_queue)
                break
            else:
                cur_node = next_node
        full_run_map[key] = cur_node
    return full_run_map

def process_first_run2(tar, map_dict, turns):
    full_run_map = {}
    for key in map_dict.keys():
        cur_node = key
        turn_queue = list(turns)
        num_to_end = 0
        while len(turn_queue) > 0:
            next_node = make_move(cur_node, turn_queue.pop(0), map_dict)
            if next_node.endswith(tar):
                num_to_end = len(turns) - len(turn_queue)
                cur_node = next_node
            else:
                cur_node = next_node
        full_run_map[key] = (num_to_end,cur_node,cur_node)
    return full_run_map


def next_runs(ori, run_map, incomplete, complete, num_turns):
    while ori in incomplete:
        check_node = incomplete.pop(0)
        if run_map[check_node] in complete:
            run_map[check_node] = run_map[run_map[check_node]] + num_turns
            complete.append(check_node)
        else:
            incomplete.append(check_node)

    return run_map

def next_runs2(run_map, incomplete, complete, num_turns):
    while len(incomplete)>0:
        check_node = incomplete.pop(0)
        if run_map[check_node][1] in complete:
            run_map[check_node] = (run_map[run_map[check_node][1]][0] + num_turns, run_map[check_node][1], run_map[run_map[check_node][1]][2])
            complete.append(check_node)
        else:
            incomplete.append(check_node)

    return run_map

def LCMofArray(a):
  lcm = a[0]
  for i in range(1,len(a)):
    lcm = lcm*a[i]//math.gcd(lcm, a[i])
  return lcm


def part1(file, part=1):
    parsed_file = parse_file(file, part)
    turn_order = parsed_file[0]
    num_turns = len(turn_order)
    path_dict = parsed_file[1]
    first_run_dict = process_first_run("ZZZ", path_dict, turn_order)
    processed_nodes = [x for x, y in first_run_dict.items() if type(y) == int]
    incomplete_nodes = [x for x, y in first_run_dict.items() if type(y) != int]
    first_run_dict = next_runs("AAA", first_run_dict, incomplete_nodes, processed_nodes, num_turns)
    return first_run_dict["AAA"]


def part2(file, part=2):
    parsed_file = parse_file(file, part)
    turn_order = parsed_file[0]
    num_turns = len(turn_order)
    path_dict = parsed_file[1]
    first_run_dict = process_first_run2("Z", path_dict, turn_order)
    processed_nodes = [x for x, y in first_run_dict.items() if y[0]>0]
    incomplete_nodes = [x for x, y in first_run_dict.items() if y[0]==0]
    first_run_dict = next_runs2(first_run_dict, incomplete_nodes, processed_nodes, num_turns)
    z_dict = {}
    a_dict = {}
    As = [(x, y) for x, y in first_run_dict.items() if x.endswith("A")]
    Zs = [(x, y) for x, y in first_run_dict.items() if x.endswith("Z")]
    for item in Zs:
        z_dict[item[0]] = item[1][0]
    for item in As:
        a_dict[item[0]] = (item[1][0],z_dict[item[1][2]])

    multiple_arr = [x[0] for x in a_dict.values()]
    return LCMofArray(multiple_arr)





t0 = time.time()
answer1 = part1('C:/Users/abrumleve4982/Documents/PycharmProjects/2023AOC/Day8/input', 1)
t1 = time.time()
answer2 = part2('C:/Users/abrumleve4982/Documents/PycharmProjects/2023AOC/Day8/input',2)
t2 = time.time()


print(f"The first answer is {answer1} - Processing time: {t1 - t0}s")
print(f"The second answer is {answer2} - Processing time: {t2-t1}s")

file = 'C:/Users/abrumleve4982/Documents/PycharmProjects/2023AOC/Day8/input'
part = 1

import networkx as nx
import matplotlib.pyplot as plt
parsed_file = parse_file(file, part)
turn_order = parsed_file[0]
num_turns = len(turn_order)
graph_dict = parsed_file[1]


# Create a directed graph
G = nx.DiGraph()

# Add edges to the graph based on the dictionary
for node, neighbors in graph_dict.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)
# Define node colors
node_colors = {}
for a in As:
    node_colors[a[0]]="Green"
for z in Zs:
    node_colors[z[0]]="Red"
# Visualize the graph
pos = nx.spring_layout(G)  # You can try different layout algorithms
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=350, node_color=[node_colors.get(node, 'skyblue') for node in G.nodes], arrowsize=20)

# Display the plot
plt.show()
