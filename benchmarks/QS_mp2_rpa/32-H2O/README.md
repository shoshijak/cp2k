# Quickstep Moeller-Plesset perturbation theory to 2nd order Random-Phase Approximation - 32 H2O

## Description of Input Files

- [`RI-MP2.inp`](RI-MP2.inp): farming input for measuring MP2 time
- [`RI-RPA.inp`](RI-RPA.inp): farming input for measuring RPA time

### Additional files

- [`BASIS_H2O`](BASIS_H2O): contains the primary and auxiliary(RI) basis sets
- [`H2O-32.xyz`](H2O-32.xyz): geometry in xyz format
- [`H2O-32-PBE-TZ.inp`](H2O-32-PBE-TZ.inp): needed to generate an initial DFT wfn (RPA, MP2)
- [`H2O-32-HF-TZ.inp`](H2O-32-HF-TZ.inp): needed to refine DFT wfn at HF level (MP2)
- [`H2O-32-RI-MP2-TZ.inp`](H2O-32-RI-MP2-TZ.inp): actual RI-MP2 benchmark (MP2)
- [`H2O-32-RI-dRPA-TZ.inp`](H2O-32-RI-dRPA-TZ.inp): actual RI-RPA benchmark (RPA)

the additional files [`t_c_g.dat`](../../../data/t_c_g.dat) and [`POTENTIAL`](../../../data/POTENTIAL) are taken from [cp2k/data](../../../data) directory.

## How to Run the Benchmark

1) run `H2O-32-PBE-TZ.inp`: this will generate the file `H2O-32-PBE-TZ-RESTART.wfn`, necessary for the two benchmark runs.
2) run `H2O-32-RI-MP2-TZ.inp` for the RI-MP2 benchmark.
3) and/or run `H2O-32-RI-dRPA-TZ.inp` for the RI-RPA benchmark.

## Results

### Results on Piz Dora, CSCS

| Input File | Configuration             | Total Number of Cores| Runtime [s]  |
| ---------- | -------------------------:| --------------------:| ------------:|
| RI-MP2.inp | 16 nodes x 16 MPI x 1 OMP |                  256 |          392 |
| RI-RPA.inp | 16 nodes x 16 MPI x 1 OMP |                  256 |          221 |

*) The timings have been obtained on CRAY-XC40 (PizDora@CSCS)

### Results on Piz Daint, CSCS (GPU partition)

Following results were obtained in the following conditions:

- Date: 12th February 2020
- CP2K version: version 7.0 (Development Version, git:78cea8eeebb25e459941d8a28d987c9990d92676)
- DBCSR version: v2.0.0-rc9 (git:15fdaba855385f12db7599a6e69b51a7a4ce8a9a)
- CP2K flags: omp libint fftw3 libxc elpa parallel mpi3 scalapack acc pw_cuda xsmm dbcsr_acc max_contr=4
- Machine: Piz Daint (GPU partition), CSCS
- The cell contents specify the runtime (`grep 'CP2K    ' output.out`) in seconds.

| Input File       | Number of Nodes | Slurm Configuration    | Runtime [s]  |
| ---------------- | ---------------:| ----------------------:| ------------:|
| H2O-32-RI-RPA-TZ | 1 node          | 2 MPI x 6 OMP per node |         1928 |
| H2O-32-RI-RPA-TZ | 1 node          | 4 MPI x 6 OMP per node |         1186 |
| H2O-32-RI-RPA-TZ | 2 nodes         | 2 MPI x 6 OMP per node |          984 |
| H2O-32-RI-RPA-TZ | 2 nodes         | 4 MPI x 6 OMP per node |          612 |
| H2O-32-RI-RPA-TZ | 4 nodes         | 2 MPI x 6 OMP per node |          506 |
| H2O-32-RI-RPA-TZ | 4 nodes         | 4 MPI x 6 OMP per node |          326 |


### Results on Piz Daint, CSCS (CPU partition)

Following results were obtained in the following conditions:

- Date: 12th February 2020
- CP2K version: version 7.0 (Development Version, git:78cea8eeebb25e459941d8a28d987c9990d92676)
- DBCSR version: v2.0.0-rc9 (git:15fdaba855385f12db7599a6e69b51a7a4ce8a9a)
- CP2K flags: omp libint fftw3 libxc elpa parallel mpi3 scalapack xsmm max_contr=4
- Machine: Piz Daint (CPU partition), CSCS
- The cell contents specify the runtime (`grep 'CP2K    ' output.out`) in seconds.

| Input File       | Number of Nodes | Slurm Configuration    | Runtime [s]  |
| ---------------- | ---------------:| ----------------------:| ------------:|
| H2O-32-RI-RPA-TZ | 1 node          | 4 MPI x 9 OMP per node |          895 |
| H2O-32-RI-RPA-TZ | 2 nodes         | 4 MPI x 9 OMP per node |          472 |
| H2O-32-RI-RPA-TZ | 4 nodes         | 4 MPI x 9 OMP per node |          254 |


