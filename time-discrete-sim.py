#!/usr/bin/env python3

import argparse
import copy
import random
import timeit

from lib.config import CONFIG
from lib.discrete_event_sim import DiscreteEventSim
from lib.node import NodeConfig, default_generate_node_list

conf = CONFIG

def run_discrete_sim_timeit(nr_nodes: int, n_times: int):
    def init_and_run_discrete_sim():
        random.seed(conf.SEED) # arbitrary seed rng for consistency between runs
        sim = DiscreteEventSim(conf, node_configs)
        sim.run_simulation()
        # include getting results, since a sim isn't useful unless we have results.
        results = sim.get_results()

        return results

    random.seed(conf.SEED) # get consistent default node list

    conf.NR_NODES = nr_nodes
    conf.update_router_dependencies()
    node_configs = default_generate_node_list(conf)

    # number set to 1, since this is heavy weight enough that a single run will take
    # an easily visible time
    results = timeit.repeat('init_and_run_discrete_sim()', repeat=parsed_arguments.n_times, number=1, globals=locals())

    # take average ignoring 5 slowest runs, assuming some other very unlucky things were happening
    # on the system.
    results.sort()
    average_without_slowest_outliers = sum(results[:-5]) / len(results[:-5])

    report = {
        'fastest': results[0],
        'modified_average': average_without_slowest_outliers,
        'all_results': results
    }

    return report

parser = argparse.ArgumentParser(
    description='basic benchmark of discrete simulation. Uses timeit, which disables garbage collection by default.'
    )
parser.add_argument('nr_nodes', type=int, help='number of nodes to generate')
parser.add_argument('n_times', nargs='?', type=int, default=25, help='number of times to run a discrete sim to gather timing data')

parsed_arguments = parser.parse_args()

# do timing run using timeit. More involved profiling should use cProfile
print(f"running default configuration discrete sim of {parsed_arguments.nr_nodes} nodes, {parsed_arguments.n_times} times")

results = run_discrete_sim_timeit(parsed_arguments.nr_nodes, parsed_arguments.n_times)

print(f"fastest time (in seconds): {results['fastest']}")
print(f"average time (in seconds), ignoring slowest outliers: {results['modified_average']}")
print(f"{results['all_results']=}")
