# part 1
import numpy

with open("day10.txt") as df:
    joltages = df.read().splitlines()

# convert from str to int and sort
joltages = list(map(int, joltages))
joltages.sort()

# add airplane chair, device adapter (store into a separate variable)
joltages.insert(0, 0)
device_adapter = joltages[-1] + 3
joltages.append(device_adapter)

differences={0:0, 1:0, 2:0, 3:0}

# Python, I want my switch!
for i in range(1, len(joltages)):
    if joltages[i] - joltages[i-1] == 0:
        differences[0] += 1
    elif joltages[i] - joltages[i-1] == 1:
        differences[1] += 1
    elif joltages[i] - joltages[i-1] == 2:
        differences[2] += 1
    elif joltages[i] - joltages[i-1] == 3:
        differences[3] += 1

print(f"The desired number is {str(differences[1] * differences[3])}")

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

# all possible connections to an adapter in form {adapter: connections}
connections = {}
for adapter in joltages:
    connections[adapter] = [a for a in joltages if 0 < a - int(adapter) <= 3]

# reverse connections, i.e. all possible ways to get to an adapter in form {adapter: sources}
reverse_connections = {}
for adapter in joltages:
    intermediate = []
    for a in connections:
        if adapter in connections[a]:
            intermediate.append(a)
    reverse_connections[adapter] = intermediate

def reverse_counter(end, begin): # counts possible paths from begin to end (only for nodes, see below)
    returner = 0
    for adapter in [i for i in reverse_connections[end] if int(i) >= int(begin)]: # consider possible sources but not those that come before begin
        if adapter == begin:
            returner += 1 # path length = 1
        else:
            returner += reverse_counter(adapter, begin) # path length = sum of possible paths to adapter
    return returner

# find "nodes" (points that are necessarily included in the chain, e.g. 0, device_adapter)
nodes = [0] # the first element is necessary

# those that are 3 apart with nothing in between are both necessary / inevitable
for e in joltages:
    if e+3 in joltages and e+1 not in joltages and e+2 not in joltages:
        if e not in nodes: # yes this could be made more efficient, but have you seen lines 36-48?
            nodes.append(e)
        if e+3 not in nodes:
            nodes.append(e+3)

if device_adapter not in nodes:
    nodes.append(device_adapter) # the last element is necessary

# find the number of ways to get to each node from the previous node
ways_to_nodes = []
for i in range(1,len(nodes)):
    ways_to_nodes.append(reverse_counter(nodes[i], nodes[i-1])) # 0-first, first-second etc.

chain_counter = numpy.prod(ways_to_nodes) # from combinatorics, all possible paths are prod of paths between "nodes"

print(f"The total number of chains is {chain_counter}")
