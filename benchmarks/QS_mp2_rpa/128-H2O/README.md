# Quickstep Moeller-Plesset perturbation theory to 2nd order Random-Phase Approximation - 128 H2O

## Description of Input Files

- [`H2O-128-PBE-TZ.inp`](H2O-128-PBE-TZ.inp): needed to generate an initial wfn for the SCF runs
- [`H2O-128-RI-dRPA-TZ.inp`](H2O-128-RI-dRPA-TZ.inp): actual RI-dRPA benchmark

## Additional files

- [`BASIS_H2O`](BASIS_H2O): contains the primary and auxiliary(RI) basis sets
- [`POTENTIAL_H2O`](POTENTIAL_H2O): contains the GTH pseudo potentials
- [`H2O-128.xyz`](H2O-128.xyz): geometry in xyz format

## How to Run the Benchmark

1) run `H2O-128-PBE-TZ.inp`: this will generate the file `H2O-128-PBE-TZ-RESTART.wfn`, necessary for the benchmark run.
2) run `H2O-128-RI-dRPA-TZ.inp` for the RI-RPA benchmark.

## Results

### Results on Piz Daint, CSCS (GPU partition)

| Input File             | Date       | CP2K Git SHA | Number of nodes | Node Configuration  | Runtime |
| ---------------------- | ---------- | ------------:| ---------------:| ------------------- | ------- |
| H2O-128-PBE-TZ.inp     | 2019-08-19 | 4519a8ad7    | 4 nodes         | 12 MPI x 1 OMP      | ~2 min  |
| H2O-128-RI-dRPA-TZ.inp | 2019-08-19 | 4519a8ad7    | 128 nodes       | 2 MPI x 6 OMP       | 80 min  |
| H2O-128-RI-dRPA-TZ.inp | 2019-12-03 | 78cea8eee    | 1024 nodes      | 2 MPI x 6 OMP       | 487 sec |

*) The timings have been obtained on CRAY-XC50 (PizDaint@CSCS, GPU partition)

### Results on Piz Daint, CSCS (CPU partition)

Following results were obtained in the following conditions:

- Date: 12th February 2020
- CP2K version: version 7.0 (Development Version, git:78cea8eeebb25e459941d8a28d987c9990d92676)
- DBCSR version: v2.0.0-rc9 (git:15fdaba855385f12db7599a6e69b51a7a4ce8a9a)
- CP2K flags: omp libint fftw3 libxc elpa parallel mpi3 scalapack xsmm max_contr=4
- Machine: Piz Daint (CPU partition), CSCS
- The cell contents specify the runtime (`grep 'CP2K    ' output.out`) in seconds, while the cells marked with an `X` crashed with out-of-memory errors, and the cells left empty weren't measured.

| Input File             | Number of Nodes | Slurm Configuration    | Runtime [s]  |
| ---------------------- | ---------------:| ----------------------:| ------------:|
| H2O-128-RI-dRPA-TZ.inp | 128 nodes       | 4 MPI x 9 OMP per node |         2043 |

*) The timings have been obtained on CRAY-XC40 (PizDaint@CSCS, CPU partition)

