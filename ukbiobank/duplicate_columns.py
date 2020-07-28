#!python3
# Duplicate values in first column of .tsv
# Add to second column
# For use in plink extraction
import sys,os
import csv
infile = sys.argv[1]
outfile = sys.argv[2]
# Loop through lines in fam
# copy first column ID
# write duplicated IDs to output
with open(infile) as fam:
    with open(outfile,"w") as out:
        df = csv.reader(fam, delimiter="\t")
        for line in df:
            fam_id_line = line[1] # e.g. A550484-4217356-050915-782_D02
            fam_id = fam_id_line.split("-")[1] # e.g. 4217356
            col = [fam_id,fam_id] # e.g. [4217356, 4217356]
            for item in col:
                out.write("%s\t" % item) # make .tsv
            out.write("\n")
        out.close()
    fam.close()
