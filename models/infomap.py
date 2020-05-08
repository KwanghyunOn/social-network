import infomap
import json
from .interface import DetectionModel


class Infomap(DetectionModel):
    def __init__(self):
        super().__init__()

    def load(self, filepath):
        self.graph = infomap.Infomap()
        self.graph.read_file(filepath)

    def run(self):
        self.graph.run()
        partition = dict()
        for node in self.graph.tree:
            if node.is_leaf:
                if node.module_id not in partition:
                    partition[node.module_id] = list()
                partition[node.module_id].append(node.node_id)
        self.community_list = list(partition.values())


if __name__ == "__main__":
    loadpath = "datasets/soc-karate.edges"
    savepath = "results/karate_infomap.json"
    im = Infomap()
    im.load(loadpath)
    im.run()
    print(im.community_list)
    im.save_result(savepath)
