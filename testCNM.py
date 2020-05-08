import snap
import json


def load(root, separator):
    graph = snap.LoadEdgeList(snap.PUNGraph, root, 0, 1, separator)
    return graph


def test_cnm(graph):
    snap.DelSelfEdges(graph)
    CmtyV = snap.TCnComV()
    modularity = snap.CommunityCNM(graph, CmtyV)
    return modularity, CmtyV


def test_girvan_newman(graph):
    CmtyV = snap.TCnComV()
    modularity = snap.CommunityGirvanNewman(graph, CmtyV)
    return modularity, CmtyV


def show_result(modularity, CmtyV):
    print(f"modularity: {modularity:.3f}")


def calc_modularity(graph, partition):
    # partition is dictionary of lists
    mod = 0
    for community in partition.values():
        nodes = snap.TIntV()
        for node in community:
            nodes.Add(node)
        mod += snap.GetModularity(graph, nodes)
    return mod
    

if __name__ == "__main__":
    root = "datasets/soc-karate.edges"
    separator = " "
    graph = load(root, separator)

    print("Girvan Newman")
    modularity, CmtyV = test_girvan_newman(graph)
    show_result(modularity, CmtyV)
    
    graph = load(root, separator)
    dict_path = "infomap_result.json"
    with open(dict_path) as json_file:
        partition = json.load(json_file)
    print(calc_modularity(graph, partition))

    graph = load(root, separator)
    dict_path = "louvain_result.json"
    with open(dict_path) as json_file:
        partition = json.load(json_file)
    print(calc_modularity(graph, partition))