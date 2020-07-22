import sys,os

bim=sys.argv[1]
for line in open(bim,"r").xreadlines():    
    line=line.strip()
    rs=line.split("\t")[1]
    a1=line.split("\t")[4]
    a2=line.split("\t")[5]
    if (len(a1)  == 1) and (len(a2) ==1):
        print rs
    else:
        pass
