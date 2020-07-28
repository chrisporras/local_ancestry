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
            fam_id = line[0]
            col = [fam_id,fam_id]
            for item in col:
                out.write("%s\t" % item)
            out.write("\n")
        out.close()
    fam.close()
