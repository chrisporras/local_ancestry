# A task list
## TODO
- [ ] Prep reference panel (TGP?)
- [ ] Use [`RFMix`](https://sites.google.com/site/rfmixlocalancestryinference/) for ibd calling
- [ ] Make stacked barplot of "painted" genomes
- [ ] Plot PCs

## Completed
- [x] Convert .bgen files to .vcf (i.e. 0,1 matrix)
- [x] Subset non-European populations
- [x] Look in scrips/ for workflow on cluster
## Notes
UKBioBank data located in regen2 node in path: `/sc/arion/projects/ipm2/christian/`

`phased_genotypes/` contains .bgen files

`scripts/` contains old sample scripts for prepping genotype data for RFMix. Look through this and model workflow off of it (will need to update paths).

`metadata/` contains reference panel labels

`genetic_maps/` is empty but will contain RFMix input map for painting.
