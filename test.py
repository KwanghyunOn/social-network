from models import CNM, Infomap, Louvain, GirvanNewman
from models.utils import calc_modularity


def run(model, datapath, savepath):
    model.load(datapath)
    model.run()
    model.save_result(savepath)
    print(calc_modularity(datapath, model.community_list))


if __name__ == "__main__":
    datapath = "datasets/fb-pages-politician.edges"
    print("Infomap")
    run(Infomap(), datapath, "results/karate-infomap.json")
    print("Louvain")
    run(Louvain(), datapath, "results/karate-louvain.json")
    print("CNM")
    run(CNM(), datapath, "results/karate-cnm.json")
    # print("GirvanNewman")
    # run(GirvanNewman(), datapath, "results/karate-girvan.json")
