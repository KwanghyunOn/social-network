from models import CNM, Infomap, Louvain, GirvanNewman
from utils import calc_modularity, draw_community


def run(model, datapath, savepath):
    model.load(datapath)
    model.run()
    model.save_result(savepath + ".json")
    draw_community(datapath, model.community_list, savepath + ".png")
    print(calc_modularity(datapath, model.community_list))


if __name__ == "__main__":
    datapath = "datasets/soc-karate.edges"
    print("Infomap")
    run(Infomap(), datapath, "results/karate-infomap")
    print("Louvain")
    run(Louvain(), datapath, "results/karate-louvain")
    print("CNM")
    run(CNM(), datapath, "results/karate-cnm")
    # print("GirvanNewman")
    # run(GirvanNewman(), datapath, "results/karate-girvan.json")
