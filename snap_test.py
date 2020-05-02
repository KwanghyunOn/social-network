import snap
from datasets import datasets

graph = datasets.FBPagesPolitician().load()
snap.DelSelfEdges(graph)

print("[CNM]")
CmtyV = snap.TCnComV()
modularity = snap.CommunityCNM(graph, CmtyV)
# for Cmty in CmtyV:
#     print("Community: ")
#     for NI in Cmty:
#         print(NI, end=" ")
#     print()
print(f"The modularity of the network is {modularity}")

