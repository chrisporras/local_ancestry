bsub -q premium -P acc_ipm2 -R "rusage[mem=12000]" -W 48:00 -o bgentovcf_chr22.log < bgentovcf_chr22.pbs
