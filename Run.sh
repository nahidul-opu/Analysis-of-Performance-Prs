#!/bin/bash
#SBATCH --job-name=MSR
#SBATCH --output=logs/%j.out
#SBATCH --error=logs/%j.err
#SBATCH --mail-user=<email>
#SBATCH --mail-type=END,FAIL

#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --gres=gpu:h100:2 
#SBATCH --cpus-per-task=2
#SBATCH --mem=80G
#SBATCH --time=02:30:00

mkdir -p logs

set -euo pipefail
echo "Job started on $(hostname) at $(date)"

module load StdEnv/2023 cuda/12.2
module load python/3.12

cd <path>
source venv/v/bin/activate

export PYTORCH_ALLOC_CONF=expandable_segments:True
export HF_TOKEN=<token>
export HF_HOME=$SLURM_TMPDIR/hf_cache

mkdir -p $HF_HOME


cd repo
srun python filter.py
echo "Job finished at $(date)"
