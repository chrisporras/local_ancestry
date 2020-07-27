for i in {1..22}

do

echo 'module load qctool' > bgentovcf_afrocarr_chr${i}.pbs

echo 'qctool -g /sc/arion/projects/ipm2/christian/local_ancestry/ukbiobank/phased_genotypes/bgens/ukb_hap_chr'${i}'_v2.bgen -s ukb1251_hap_chr'${i}'_v2_s487395.sample -og afro_carr_ukbb_chr'${i}'.vcf -incl-samples afro_carribean_ukbb.txt' >> bgentovcf_afrocarr_chr${i}.pbs

bsub -q premium -P acc_ipm2 -R "rusage[mem=12000]" -W 88:00 -n 1 -o bgentovcf_afrocarr_chr${i}.log < bgentovcf_afrocarr_chr${i}.pbs

done
