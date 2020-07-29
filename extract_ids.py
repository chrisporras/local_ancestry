#!python3
# Duplicate .fam ids from mapper
import sys, os
import csv
infile = sys.argv[1]
outfile = sys.argv[2]
# For each line in mapper,
# pull IDs from col 3
# duplicate in 2 output cols
# for plink subsetting
with open(infile) as map:
    with open(outfile,"w") as out:
        df = csv.reader(map, delimiter="\t")
        for line in df:
            ids = [line[0],line[0]]
            for item in ids:
                out.write("%s\t" % item)
            out.write("\n")
        out.close()
    map.close()
