#for i in {1..22}

#do

#echo 'module load python' > vcf_to_ped_chr${i}.pbs
#echo 'python vcftoped.py UKBB_chr'${i}'.noindel.vcf UKBB_chr'${i}'.noindel.ped' >> vcf_to_ped_chr${i}.pbs
#echo 'gzip UKBB_chr'${i}'.noindel.vcf' >> vcf_to_ped_chr${i}.pbs
 
#bsub -q premium -P acc_ipm2 -R "himem" -R "rusage[mem=330000]" -W 120:00 -o vcf_to_ped_chr${i}.log < vcf_to_ped_chr${i}.pbs

#done


for i in  {1..22} #17 #7 8 9 10 11 12 13 14  #1 2 3 4 5 6

do

echo 'module load python py_packages' > vcf_to_ped_chr${i}.pbs
echo 'python vcftoped.RS.py UKBB_chr'${i}'.noindel.vcf /sc/orga/projects/ipm/Gillian/ukbb_ibd/phased_plink/UKBB_chr'${i}'.noindel.ped' >> vcf_to_ped_chr${i}.pbs
echo 'gzip UKBB_chr'${i}'.noindel.vcf' >> vcf_to_ped_chr${i}.pbs

bsub -q premium -P acc_ipm2  -R "rusage[mem=55000]" -W 24:00 -o vcf_to_ped_chr${i}.log < vcf_to_ped_chr${i}.pbs
 
done
