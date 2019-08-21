#!/bin/bash -l
#
#SBATCH --job-name=RPA-init
#SBATCH --mail-type=ALL
#SBATCH --mail-user=jakobovits@cscs.ch
#SBATCH --time=00:30:00
#SBATCH --nodes=4
#SBATCH --ntasks-per-core=1
#SBATCH --ntasks-per-node=12
#SBATCH --cpus-per-task=1
#SBATCH --partition=debug
#SBATCH --constraint=gpu


export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
export CRAY_CUDA_MPS=1

srun /users/alicej/cp2k/exe/PizDaint/cp2k.psmp  H2O-64-PBE-TZ.inp

