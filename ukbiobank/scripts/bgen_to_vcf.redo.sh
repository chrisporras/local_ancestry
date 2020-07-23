for i in {22..22}

do

echo 'module load bgen' > bgentovcf_chr${i}.backup.pbs

echo 'bgenix -g /sc/orga/projects/ipm/data/UKBiobank/Genotyping/ukb_hap_chr'${i}'_v2.bgen  -incl-rsids ukb_snp_chr'${i}'_v2.noindels.snplist -vcf >> UKBB_chr'${i}'.noindel.BACKUP.vcf' >> bgentovcf_chr${i}.backup.pbs

bsub -q premium -P acc_ipm2 -R "rusage[mem=12000]" -W 88:00 -o bgentovcf_chr${i}.backup.log < bgentovcf_chr${i}.backup.pbs

done
