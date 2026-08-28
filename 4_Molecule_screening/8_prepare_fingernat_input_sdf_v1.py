#Prepare SDF input files with docking results for fingeRNAt analysis

import os
import sys
import csv
import pandas as pd
import numpy as np

inpath = sys.argv[1]
dockpath = sys.argv[2]
outpath = sys.argv[3]

for fname in os.listdir(inpath):
	target = fname.replace("_top_mols_v1.csv", "")
	df = pd.read_csv(inpath+fname, sep="\t", header=0)
	
	outfile = outpath+target+"_out.sdf"
	out = open(outfile, "w")
	
	for i, mol in df.iterrows():
		idx = 0
		with open(dockpath+target+"/"+target+"_"+mol["Ligand"]+"_out.sd") as f:
			for line in f.readlines():
				if(idx==0):
					print(str(mol["Ligand"]), file=out)
				else:
					print(line, end="", file=out)
				
				idx = idx + 1
		f.close()
		
	out.close()
	print(target)

	#break






























