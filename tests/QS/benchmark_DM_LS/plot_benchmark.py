#!/usr/bin/env python3
import os
import re
import argparse
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# -------------------------------------------------------------------------------------
def main(result_file, node_to_plot, nrep_to_plot):
    print("Program parameters:", result_file, node_to_plot, nrep_to_plot)

    # Read and parse file into a pandas Dataframe
    results = parse_file(result_file)

    # Plot results
    plot_benchmark(results, node_to_plot, nrep_to_plot)

# -------------------------------------------------------------------------------------
# e.g. slurm-H2O-dft-ls.n1.12659210.o:42: CP2K| Input file name                                      H2O-dft-ls.NREP1.inp
input_file_description = re.compile(
    r'slurm-.*.n(?P<nnodes>\d+)(.*)?.\d+.o:\d+: CP2K\| Input file name\s+H2O-(dft-ls|md).NREP(?P<nrep>\d+)(.*)?.inp')
# e.g. slurm-H2O-dft-ls.n1.12659210.o-905- CP2K\s+1\s+1.0    0.038    0.038    8.814    8.814
total_time = re.compile(
    r'slurm-.*.n(?P<nnodes>\d+)(.*)?.\d+.o-\d+- CP2K\s+1\s+1.0\s+\d+.\d+\s+\d+.\d+\s+\d+.\d+\s+(?P<time>\d+.\d+)')
def parse_file(file):
    """
    Typical use case: on daint in `~/cp2k/tests/QS/benchmark_DM_LS/bench_H2O-dft-ls`: 
    Run `grep -A2 -Pn '(TOTAL TIME|NREP)' slurm-H2O-dft-ls.n* > results.txt` and use this as input file
    """
    with open(file) as f:
        file_content = f.readlines()

    results = list()  # of dictionaries
    for line in file_content:
        # input file description line -> get nrep
        if input_file_description.match(line): 
            nnodes = input_file_description.match(line).group('nnodes')
            nrep = input_file_description.match(line).group('nrep')

        # total time line -> get number of nodes and total time
        if total_time.match(line): 
            nnodes = total_time.match(line).group('nnodes')
            time = total_time.match(line).group('time')
            results.append({'system size (nrep)': int(nrep), 'number of nodes': int(nnodes), 'time [s]': float(time)})

    #return pd.Dataframe(results)
    return pd.DataFrame(results)


def plot_benchmark(results, node_to_plot, nrep_to_plot):
    # Plot results by number of nodes
    print("Raw data:")
    print(results.to_string(index=False))
    if node_to_plot == 0:
        node_array = list(np.unique(results['number of nodes'].values))
    else:
        node_array = [node_to_plot]
    for node in node_array:
        # Get the results of this node
        to_plot = results[results['number of nodes'] == node]
        if len(to_plot.index) > 1:
            plot_single_benchmark(to_plot, 'number of nodes', node, 'system size (nrep)', 'time [s]')

    # Plot results by system size
    if nrep_to_plot == 0:
        nrep_array = list(np.unique(results['system size (nrep)'].values))
    else:
        nrep_array = [nrep_to_plot]
    for nrep in nrep_array:
        to_plot = results[results['system size (nrep)'] == nrep]
        if len(to_plot.index) > 1:
            plot_single_benchmark(to_plot, 'system size (nrep)', nrep, 'number of nodes', 'time [s]')


def plot_single_benchmark(df, fixed_quantity, fixed_quantity_value, col_x, col_y):
    df.plot(x=col_x, y=col_y, kind='scatter', title=fixed_quantity + " = " + str(fixed_quantity_value))
    plt.show()


# -------------------------------------------------------------------------------------
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="""
        Plot pretty CP2K water benchmarks 
        """,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-f', '--file', metavar="results_file.txt", default="results.txt", type=str, help="results file to parse")
    parser.add_argument('-n', '--nodes', metavar="NUM_NODES", default=0, type=int, help="Plot only this number of nodes")
    parser.add_argument('-r', '--nrep', metavar="NREP", default=0, type=int, help="Plot only this system size (nrep)")

    args = parser.parse_args()
    main(args.file, args.nodes, args.nrep) 
