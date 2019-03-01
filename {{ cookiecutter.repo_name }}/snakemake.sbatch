#!/bin/bash

# sbatch submission script to run main snakemake process. It then submits
# individual jobs from the compute node.

#SBATCH --job-name=snakemake
#SBATCH --output=/home/bjf79/slurm_stdout_logs/project1_repo_snakemake.txt
#SBATCH --time=4-00:00:00
#SBATCH --partition=gilad
#SBATCH --mem=4G
#SBATCH --tasks-per-node=4


snakemake --jobs 200 -p --ri --use-conda --cluster-config cluster-config.json --cluster "sbatch --partition={cluster.partition} --job-name={cluster.name} --output=/dev/null --job-name={cluster.name} --nodes={cluster.n} --mem={cluster.mem}"
