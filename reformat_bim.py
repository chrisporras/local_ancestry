#!python3
# Fix formatting issue in .bim converted from vcf
import sys, os
import csv
infile = sys.argv[1]
outfile = sys.argv[2]
# For each line in bim,
# move chr number to first column
# and remove it from ID
### e.g. ". rs0000,1 0 A G" -> "1 rs0000 0 A G"
with open(infile) as bim:
    with open(outfile,"w") as out:
        df = csv.reader(bim, delimiter="\t")
        for line in df:
            line[0] = line[1].split(",")[1]
            line[1] = line[1].split(",")[0]
            for item in line:
                out.write("%s\t" % item)
            out.write("\n")
        out.close()
    bim.close()
