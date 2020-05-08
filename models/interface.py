import json


class DetectionModel:
    def __init__(self):
        self.graph = None
        self.community_list = None
        
    def load(self, filepath):
        pass

    def run(self):
        pass

    def save_result(self, filepath):
        with open(filepath, 'w') as fp:
            json.dump(self.community_list, fp)
        
