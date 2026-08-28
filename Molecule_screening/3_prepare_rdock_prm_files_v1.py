#Program to prepare RxDock parameter files for HCV virtual screening

import os
import sys
import csv
import pandas as pd
import numpy as np

inpath = sys.argv[1]
outpath = sys.argv[2]

for fname in os.listdir(inpath):
	if(fname.endswith("_receptor.mol2")):
		prm_fname = fname.replace("_receptor.mol2", "")+"_rdock.prm"
		
		out = open(outpath+prm_fname, "w")
		
		print("RBT_PARAMETER_FILE_V1.00", file=out)
		print("TITLE RNA_DOCKING", file=out)
		print("", file=out)
		print("RECEPTOR_FILE /home/hw2477663/PhD/Whole_genome_case/Related_articles/NAR_GAB/R1/Source_code/4_Molecule_screening/output/Receptors/"+fname, file=out)
		print("RECEPTOR_FLEX 3.0", file=out)
		print("", file=out)
		print("##################################################################", file=out)
		print("### CAVITY DEFINITION: REFERENCE LIGAND METHOD", file=out)
		print("##################################################################", file=out)
		print("SECTION MAPPER", file=out)
		print("    SITE_MAPPER RbtLigandSiteMapper", file=out)
		print("    REF_MOL /home/hw2477663/PhD/Whole_genome_case/Related_articles/NAR_GAB/R1/Source_code/4_Molecule_screening/output/Receptors/"+fname.replace("_receptor.mol2", "")+"_orig.sdf", file=out)
		print("    RADIUS 6.0", file=out)
		print("    SMALL_SPHERE 1.0", file=out)
		print("    MIN_VOLUME 100", file=out)
		print("    MAX_CAVITIES 1", file=out)
		print("    VOL_INCR 0.0", file=out)
		print("   GRIDSTEP 0.5", file=out)
		print("END_SECTION", file=out)
		print("", file=out)
		print("################################################################", file=out)
		print("# CAVITY DEFINITION: TWO SPHERES METHOD", file=out)
		print("################################################################", file=out)
		print("#SECTION MAPPER", file=out)
		print("#    SITE_MAPPER RbtSphereSiteMapper", file=out)
		print("##HETATM 2815  O   HOH   756      37.266 -20.992  -4.910  0.90 24.86      1CSE2940", file=out)
		print("#    CENTER (22.233,14.118.250,8.799)", file=out)
		print("#    RADIUS 50.0", file=out)
		print("#    SMALL_SPHERE 1.5", file=out)
		print("#    LARGE_SPHERE 6.0", file=out)
		print("#    MAX_CAVITIES 5", file=out)
		print("#END_SECTION", file=out)
		print("", file=out)
		print("#################################", file=out)
		print("#CAVITY RESTRAINT PENALTY", file=out)
		print("#################################", file=out)
		print("SECTION CAVITY", file=out)
		print("    SCORING_FUNCTION RbtCavityGridSF", file=out)
		print("    WEIGHT 1.0", file=out)
		print("END_SECTION", file=out)
		print("", file=out)
		print("#################################", file=out)
		print("## PHARMACOPHORIC RESTRAINTS", file=out)
		print("#################################", file=out)
		print("#SECTION PHARMA", file=out)
		print("#    SCORING_FUNCTION RbtPharmaSF", file=out)
		print("#    WEIGHT 1.0", file=out)
		print("#    CONSTRAINTS_FILE pharma_cdk2.const", file=out)
		print("#   OPTIONAL_FILE optional.const", file=out)
		print("#   NOPT 3", file=out)
		print("#   WRITE_ERRORS TRUE", file=out)
		print("#END_SECTION", file=out)
		
		out.close()
		
		print(fname)





























