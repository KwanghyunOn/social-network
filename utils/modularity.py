import snap


def calc_modularity(filepath, community_list):
    graph = snap.LoadEdgeList(snap.PUNGraph, filepath, 0, 1, " ")
    modularity = 0
    for community in community_list:
        nodes = snap.TIntV()
        for node in community:
            nodes.Add(node)
        modularity += snap.GetModularity(graph, nodes)
    return modularity
