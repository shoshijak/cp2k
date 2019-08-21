#!/bin/bash -l
#
#SBATCH --job-name=RPA-final
#SBATCH --mail-type=ALL
#SBATCH --mail-user=jakobovits@cscs.ch
#SBATCH --time=01:00:00
#SBATCH --nodes=128
#SBATCH --ntasks-per-core=1
#SBATCH --ntasks-per-node=2
#SBATCH --cpus-per-task=6
#SBATCH --partition=normal
#SBATCH --constraint=gpu


export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
export CRAY_CUDA_MPS=1

srun -u /users/alicej/cp2k/exe/PizDaint-print-for-marko/cp2k.psmp H2O-128-RI-dRPA-TZ.inp

