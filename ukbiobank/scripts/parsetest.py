import sys,os

# try different way of doing it

rsids = []
genotypes = []


infile = sys.argv[1]
outf=sys.argv[2]

for line in file(infile):
	if line.startswith('##'):
		continue
	elif line.startswith('FORMAT'):
		continue
	elif line.startswith('#CHROM'):
		line = line.strip().split()
		# header line with indivs etc
		indivs = line[9:]
		print 'found %s individuals' % (len(indivs))
	else:
		# in main data
		line = line.strip().split()
		rsids.append(line[2])
		# hard-code vcf format for now with no chromosome...
		vcfgenos = line[8:]
		genoline = [vcfgeno[0] + "\t" + vcfgeno[2] for vcfgeno in vcfgenos]
		genotypes.append(genoline)

# now, flip data around to write it
print 'transposing %s genotypes' % (len(genotypes))
genos = zip(*genotypes)
outfile = file(outf , 'w')
print 'writing output to %s' % (outfile)
for i, indiv in enumerate(indivs):
	outfile.write('%s\t%s\t0\t0\t0\t0\t%s\n' % (indiv, indiv, '\t'.join(genos[i]).replace('1','2').replace('0','1')))
		
