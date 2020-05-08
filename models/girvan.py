import snap
import json
from .interface import DetectionModel


class GirvanNewman(DetectionModel):
    def __init__(self):
        super().__init__()

    def load(self, filepath):
        self.graph = snap.LoadEdgeList(snap.PUNGraph, filepath, 0, 1, " ")

    def run(self):
        snap.DelSelfEdges(self.graph)
        community_list = snap.TCnComV()
        snap.CommunityGirvanNewman(self.graph, community_list)

        self.community_list = list()
        for community in community_list:
            cmty = list()
            for node in community:
                cmty.append(node)
            self.community_list.append(cmty)
