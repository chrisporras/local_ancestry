for i in {1..22}

do

tail -n +6  UKBB_chr${i}.noindel.vcf | cut -f1-4 | awk -F $'\t' -v i="${i}" '{print i,$3" 0 "$2}' > UKBB_chr${i}.noindel.map

done

