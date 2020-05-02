import snap


def load(root, separator):
    graph = snap.LoadEdgeList(snap.PUNGraph, root, 0, 1, separator)
    return graph


def testCNM(graph):
    snap.DelSelfEdges(graph)
    CmtyV = snap.TCnComV()
    modularity = snap.CommunityCNM(graph, CmtyV)
    for Cmty in CmtyV:
        print("Community: ")
        for NI in Cmty:
            print(NI, end=" ")
        print()
    print(f"The modularity of the network is {modularity}")


if __name__ == "__main__":
    root = "datasets/fb-pages-politician.edges"
    separator = ","
    testCNM(load(root, separator))