import community as community_louvain
import networkx as nx
from .interface import DetectionModel


class Louvain(DetectionModel):
    def __init__(self):
        super().__init__()

    def load(self, filepath):
        self.graph = nx.read_edgelist(filepath, delimiter=" ")

    def run(self):
        partition = community_louvain.best_partition(self.graph)
        par_rev = dict()
        for node, com in partition.items():
            if com not in par_rev:
                par_rev[com] = list()
            par_rev[com].append(int(node))
        self.community_list = list(par_rev.values())


if __name__ == "__main__":
    loadpath = "datasets/soc-karate.edges"
    savepath = "results/karate_louvain.json"
    
    louvain = Louvain()
    louvain.load(loadpath)
    louvain.run()
    print(louvain.community_list)
    louvain.save_result(savepath)
