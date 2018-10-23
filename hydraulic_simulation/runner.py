import json
from epanettools import epanet2 as et

from controller import Controller
from data_util import ComponentConfig, TasMaxProfile

net_file = "../data/north_marin_c.inp"
output_file = "../output/output_nmc.rpt"

comps = ComponentConfig("../data/cdf/elec_best_cdf.txt", "../data/cdf/motor_best_cdf.txt",
                        "../data/cdf/iron_best_cdf.txt", "../data/cdf/pvc_best_cdf.txt")
tasmax = TasMaxProfile('../data/temperature/2017_2099_rcp_4.5_avg.csv')

example = Controller(net_file, output_file, tasmax)
example.populate(comps)
print("Pipe Count: ", len(example.pipes), "\tPump Count: ", len(example.pumps))

example.run()

pres_by_node = dict({(node_.id_, tuple(node_.pressure))
                     for node_ in example.nodes})
json.dump(pres_by_node, open('../output/pressure_by_node.json', 'w+'))
