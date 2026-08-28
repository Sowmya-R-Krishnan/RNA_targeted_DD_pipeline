#Run fingeRNAt analysis and gather results

import os
import sys
import csv
import pandas as pd
import numpy as np

inpath = sys.argv[1]
pdbpath = sys.argv[2]

for fname in os.listdir(inpath):
	target = fname.replace("_out.sdf", "")
	
	os.system("python ./fingernat/code/fingeRNAt.py -r "+pdbpath+target+".pdb -l "+inpath+fname+" -dha -detail")
	
	print(fname)
	

	
