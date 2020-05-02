import abc
import snap


class Dataset:
    def __init__(self):
        self.root = None
        self.separator = None

    @abc.abstractmethod
    def load(self):
        pass


class KarateClub(Dataset):
    def __init__(self):
        super().__init__()
        self.root = "datasets/soc-karate.edges"
        self.separator = " "

    def load(self):
        graph = snap.LoadEdgeList(snap.PUNGraph, self.root, 0, 1, self.separator)
        return graph


class FBPagesPolitician(Dataset):
    def __init__(self):
        super().__init__()
        self.root = "datasets/fb-pages-politician.edges"
        self.separator = ","

    def load(self):
        graph = snap.LoadEdgeList(snap.PUNGraph, self.root, 0, 1, self.separator)
        return graph
