#!/bin/bash
#SBATCH -J qsm
#SBATCH -o out.out      
#SBATCH -e error.err 
#SBATCH -p xxxx
#SBATCH --nodes=3
#SBATCH --ntasks-per-node=3
#SBATCH --cpus-per-task=40
#SBATCH --mem=120G

module purge
module load gnu12
module load mpich/3.4.3-ucx
module load gaussian/16aC.01
export GAUSS_SCRDIR="/tmp"
export PATH=/path_to_tinker_binaries/binaries:$PATH

scontrol show hostnames $SLURM_JOB_NODELIST > host_list

mpirun -np 3 --hostfile host_list lichem.MPI -n 360 -x rkt_dfp.xyz -c connect.inp -r regions.inp -o qsm.xyz -l qsm.log

