for i in {6..22}

do

tail -n +6 UKBB_chr${i}.noindel.vcf > UKBB_chr${i}.noindel.vcf2
mv UKBB_chr${i}.noindel.vcf2 UKBB_chr${i}.noindel.vcf

done
