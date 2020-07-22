import sys,os

vcf=sys.argv[1]
prefix=sys.argv[2]
chr=sys.argv[3]

for line in open(vcf,"r").xreadlines():
    line=line.strip().split("\t")
    #pos=line.split("\t")[1]
    #snp=line.split("\t")[2]
    print line
