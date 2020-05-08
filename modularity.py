import snap

Nodes = snap.TIntV()
for nodeId in range(10):
    Nodes.Add(nodeId)

Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
print(snap.GetModularity(Graph, Nodes, 1000))

UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
print(snap.GetModularity(UGraph, Nodes, 1000))

Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
print(snap.GetModularity(Network, Nodes, 1000))