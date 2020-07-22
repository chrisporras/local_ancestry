import os


master={}
pts=[]
snps=[]

with open("test.mem.vcf","r") as f:
	for _ in xrange(4):
		next(f)	
	for x, line in enumerate(f):
		items=line.strip().split('\t')
		if x==0:
			pts=items[10:]
			for pt in pts:
				master[pt]=[]
		else:
			rsid=items[1]
			snps.append(rsid)
			ref=items[2]
			alt=items[3]
			items2=[a for a in items[10:] if a != ""]
			for i in xrange(len(pts)):
				j=items2[i].split(":")[0]
				k=j.replace("0",ref)
				snp=k.replace("1",alt)
				master[pts[i]].append(snp)



h=open("test2_plink.ped","w")

for pt in pts:
	h.write(str(pt) + "\t" + str(pt) + "\t0\t0\t0\t0\t")
	for i in master[pt][:-1]:
		j=i.split("|")
		h.write(str(j[0]) + '\t' + str(j[1]) + '\t')
#
	k=master[pt][-1].split("|")		
	h.write(str(k[0]) + '\t' + str(k[1]) + '\n')



h.close()	
