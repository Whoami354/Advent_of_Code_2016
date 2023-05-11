import io


# --- Day 22: Grid Computing ---
#
# You gain access to a massive storage cluster arranged in a grid; each
# storage node is only connected to the four nodes directly adjacent to
# it (three if the node is on an edge, two if it's in a corner).
#
# You can directly access data only on node /dev/grid/node-x0-y0, but
# you can perform some limited actions on the other nodes:
#
#     You can get the disk usage of all nodes (via df). The result of
#     doing this is in your puzzle input.
#
#     You can instruct a node to move (not copy) all of its data to an
#     adjacent node (if the destination node has enough space to receive
#     the data). The sending node is left empty after this operation.
#
# Nodes are named by their position: the node named node-x10-y10 is
# adjacent to nodes node-x9-y10, node-x11-y10, node-x10-y9, and
# node-x10-y11.
#
# Before you begin, you need to understand the arrangement of data on
# these nodes. Even though you can only move data between directly
# connected nodes, you're going to need to rearrange a lot of the data
# to get access to the data you need. Therefore, you need to work out
# how you might be able to shift data around.
#
# To do this, you'd like to count the number of viable pairs of nodes. A
# viable pair is any two nodes (A,B), regardless of whether they are
# directly connected, such that:
#
#     Node A is not empty (its Used is not zero).
#     Nodes A and B are not the same node.
#     The data on node A (its Used) would fit on node B (its Avail).
#
# How many viable pairs of nodes are there?

# Datastructure for a node:
# ((x, y), size, used, avail, use)

def to_int(item):
    """
    Turns into into an item ending with a special character, e.g., '94T' is
    turned into 94, '71%' is turned into 71.
    """
    return int(item[:-1])


def parse_node(line):
    content = line.split()

    node = content[0].split('-')
    x = int(node[1][1:])
    y = int(node[2][1:])
    coords = (x, y)

    size = to_int(content[1])
    used = to_int(content[2])
    avail = to_int(content[3])

    return (coords, size, used, avail)


def is_viable_pair(nodeA, nodeB):
    # Nodes A and B are not the same node.
    # Node A is not empty (its Used is not zero).
    # The data on node A (its Used) would fit on node B (its Avail).
    return nodeA != nodeB and nodeA[2] != 0 and nodeA[2] <= nodeB[3]


with io.open('input', 'r') as f:
    # Loading nodes
    lines = f.readlines()
    i = 2  # skipping the two first lines
    nodes = []
    for i in range(2, len(lines)):
        node = parse_node(lines[i])
        nodes.append(node)

    viable_pairs = []
    for nodeA in nodes:
        for nodeB in nodes:
            if is_viable_pair(nodeA, nodeB):
                viable_pairs.append((nodeA, nodeB))

    print('Number of viable pairs: {}'.format(len(viable_pairs)))