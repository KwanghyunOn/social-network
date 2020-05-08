import community as community_louvain
import networkx as nx
import matplotlib.pyplot as plt
import json


def load(root, delimiter):
    G = nx.read_edgelist(root, delimiter=delimiter)
    return G


if __name__ == "__main__":
    root = "datasets/soc-karate.edges"
    delimiter = " "
    G = load(root, delimiter=delimiter)
    print(f"V = {G.number_of_nodes()}, E = {G.number_of_edges()}")
    partition = community_louvain.best_partition(G)
    par_rev = dict()
    for node, com in partition.items():
        if com not in par_rev:
            par_rev[com] = list()
        par_rev[com].append(int(node))
    
    save_path = "louvain_result.json"
    with open(save_path, 'w') as fp:
        json.dump(par_rev, fp)

# #drawing
# size = float(len(set(partition.values())))
# pos = nx.spring_layout(G)
# count = 0.
# for com in set(partition.values()) :
#     count = count + 1.
#     list_nodes = [nodes for nodes in partition.keys()
#                                 if partition[nodes] == com]
#     nx.draw_networkx_nodes(G, pos, list_nodes, node_size = 20,
#                                 node_color = str(count / size))


# nx.draw_networkx_edges(G, pos, alpha=0.5)
# plt.show()



# import community as lvcm
#
#
# """ Louvain method """
# partition = lvcm.best_partition(graph=G, partition=None, weight='weight', resolution=1., randomize=True)
# max_k_w = []
# for com in set(partition.values()):
#     list_nodes = [nodes for nodes in partition.keys()
#                   if partition[nodes] == com]
#     max_k_w = max_k_w + [list_nodes]
#
# """ Make Community Color list """
# community_num_group = len(max_k_w)
# color_list_community = [[] for i in range(len(G.nodes()))]
# for i in range(len(G.nodes())):
#     for j in range(community_num_group):
#         if i in max_k_w[j]:
#             color_list_community[i] = j
#
# """ Plot Community """
# fig = plt.figure()
# edges = G.edges()
# weights = [G[u][v]['weight'] for u, v in edges]
# Feature_color_sub = color_list_community
# node_size = 50
# im = nx.draw_networkx_nodes(G, pos, node_size=node_size, node_color=Feature_color_sub, cmap='jet', vmin=0, vmax=community_num_group)
# nx.draw_networkx_edges(G, pos, width=weights)
# nx.draw_networkx_labels(G, pos, font_size=5, font_color="black")
# plt.xticks([])
# plt.yticks([])
# plt.colorbar(im)
# plt.show(block=False)