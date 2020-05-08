from infomap import Infomap
import json


def show_result(im):
    print(f"Found {im.num_top_modules} modules with codelength: {im.codelength}")
    partition = dict()
    for node in im.tree:
        if node.is_leaf:
            print(f"({node.module_id}, {node.node_id})")
            if node.module_id not in partition:
                partition[node.module_id] = set()
            partition[node.module_id].add(node.node_id)
    for module, nodes in partition.items():
        print(f"[{module}]")
        for node in nodes:
            print(node, end=" ")
        print()


def save_partition(im, save_path):
    partition = dict()
    for node in im.tree:
        if node.is_leaf:
            if node.module_id not in partition:
                partition[node.module_id] = list()
            partition[node.module_id].append(node.node_id)
    with open(save_path, 'w') as fp:
        json.dump(partition, fp)
        

if __name__ == "__main__":
    im = Infomap()
    im.read_file("datasets/soc-karate.edges")
    im.run()
    save_path = "infomap_result.json"
    save_partition(im, save_path)
