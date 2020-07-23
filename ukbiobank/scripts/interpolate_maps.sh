
MAP=/sc/orga/projects/ipm2/Resources/Genetic_Map_GRCh37/



for i in {1..22}
do 

python interpolate_maps.py UKBB_chr${i}.noindel.map ${MAP}genetic_map_GRCh37_chr${i}.txt UKBB_chr${i}.noindel.genetic.map

#awk -v i="${i}" '{print i" "$1" "$3" "$2}' jhap_biome_1kg.nopalindromes_chr${i}.genetic.map > jhap_biome_1kg.nopalindromes_chr${i}.genetic.map2

done 