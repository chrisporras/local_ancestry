import sys
import os
import numpy as np
import gc
# try different way of doing it
dt = np.dtype('a1')

if __name__ == "__main__":
    rsids = []
    genotypes = []

    infile = sys.argv[1]
    outf = sys.argv[2]

    corpus = []
    people_count = 0
    rsid_count = 0
    with file(infile) as input_vcf:
        for line in input_vcf:
            if line.startswith('##'):
                continue
            elif line.startswith('FORMAT'):
                continue
            elif line.startswith('#CHROM'):
                line = line.strip().split()
                # header line with indivs etc
                indivs = line[9:]
                print 'found %s individuals' % (len(indivs))
                people_count = len(indivs)
                
            else:
                # in main data
                rsid_count += 1
        gc.collect()
    
    print "Individuals Count: ",people_count," RSID count: ",rsid_count
    geno_mat = np.zeros((people_count,rsid_count*2),dtype=dt)
    
    print "shape of the final result will be",geno_mat.shape
    rsid_index = 0 
    with file(infile) as input_vcf:
        for line in input_vcf:
            if line.startswith('##'):
                continue
            elif line.startswith('FORMAT'):
                continue
            elif line.startswith('#CHROM'):
                continue
            else:
                line = line.strip().split()
                rsids.append(line[2])
                for i in range(people_count):
                    # print type(line[8+i]
                    geno_mat[i,rsid_index*2] = line[8+i][0]
                    geno_mat[i,rsid_index*2 + 1] = line[8+i][2]
                rsid_index+= 1 
            # line = line.strip().split()
            # rsids.append(line[2])
            # # hard-code vcf format for now with no chromosome...
            # vcfgenos = line[8:]
            # genoline = [vcfgeno[0] + "\t" + vcfgeno[2] for vcfgeno in vcfgenos]
            # genotypes.append(genoline)
    with file(outf,'w') as outputfile:
        for i,indiv in enumerate(indivs):
            outputfile.write('%s\t%s\t0\t0\t0\t0\t%s\n' % (
                indiv, indiv, '\t'.join(geno_mat[i])
            ))
            
        

# # now, flip data around to write it
# print 'transposing %s genotypes' % (len(genotypes))
# genos = zip(*genotypes)
# outfile = file(outf, 'w')
# print 'writing output to %s' % (outfile)
# for i, indiv in enumerate(indivs):
#     outfile.write('%s\t%s\t0\t0\t0\t0\t%s\n' % (
#         indiv, indiv, '\t'.join(genos[i]).replace('1', '2').replace('0', '1')))
