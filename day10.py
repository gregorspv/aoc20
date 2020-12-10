# part 1
import numpy

with open("day10.txt") as df:
    joltages = df.read().splitlines()

joltages = list(map(int, joltages))
joltages.sort()

# airplane chair, device adapter
joltages.insert(0, 0)
device_adapter = joltages[-1] + 3
joltages.append(device_adapter)

diff_0 = 0
diff_1 = 0
diff_2 = 0
diff_3 = 0

for i in range(1, len(joltages)):
    if joltages[i] - joltages[i-1] == 0:
        diff_0 += 1
    elif joltages[i] - joltages[i-1] == 1:
        diff_1 += 1
    elif joltages[i] - joltages[i-1] == 2:
        diff_2 += 1
    elif joltages[i] - joltages[i-1] == 3:
        diff_3 += 1

print(f"The desired number is {str(diff_1 * diff_3)}")

# part 2

chain_counter = 0

# WORKS but SLOW
#
# def construct_chain(previous_chain):
#     global chain_counter
#     # print(chain_counter)
#
#     if previous_chain[-1] != device_adapter: # if chain is incomplete
#         for next_adapter in [a for a in list(set(joltages) - set(previous_chain)) if 0 <= a - previous_chain[-1] <= 3]:
#             construct_chain(previous_chain + [next_adapter]) # concatenation NOT append !!
#     else: # complete chain
#         chain_counter +=1
#
# construct_chain([0])

# relate all possible connections to an adapter
connections = {}
for adapter in joltages:
    connections[adapter] = [a for a in joltages if 0 < a - int(adapter) <= 3]

# make a reverse dict, i.e. all possible ways to get to an adapter
reverse_connections = {}
for adapter in joltages:
    intermediate = []
    for a in connections:
        if adapter in connections[a]:
            intermediate.append(a)
    reverse_connections[adapter] = intermediate

def reverse_counter(end, begin): # counts possible paths from begin to end
    returner = 0
    for adapter in [i for i in reverse_connections[end] if int(i) >= int(begin)]:
        # print(adapter, end, begin)
        if adapter == begin:
            returner += 1
        else:
            returner += 1 * reverse_counter(adapter, begin)
        # print(adapter, returner)
    return returner

# find nodes (points that are necessarily included in the chain, e. g. 0)
nodes = [0] # the first element is necessary

# those that are 3 apart with nothing in between are both necessary
for e in joltages:
    if e+3 in joltages and e+1 not in joltages and e+2 not in joltages:
        if e not in nodes: # yes it is inefficient, but have you seen lines 36-48?
            nodes.append(e)
            nodes.append(e+3)

if device_adapter not in nodes:
    nodes.append(device_adapter) # the last element is necessary

# find the number of ways to get to each node from the previous node
ways_to_nodes = []
for i in range(1,len(nodes)):
    ways_to_nodes.append(reverse_counter(nodes[i], nodes[i-1]))

chain_counter = numpy.prod(ways_to_nodes)

print(f"The total number of chains is {chain_counter}")
