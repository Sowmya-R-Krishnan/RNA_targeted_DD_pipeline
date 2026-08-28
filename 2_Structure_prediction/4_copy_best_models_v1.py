#Copy the best models (based on energy) to a new folder

import os
import sys
import csv
import pandas as pd
import numpy as np

inpath = sys.argv[1]
ene_logs = sys.argv[2]
outpath = sys.argv[3]

regions = ["49_114", "592_663", "762_816", "1010_1050", "1277_1293", "1320_1534", "2049_2117", "2287_2362", "2520_2561", "3293_3362", "3716_3799", "3864_3895", "4558_4671", "4873_4968", "5297_5411", "5444_5499", "5807_5876", "5999_6074", "6518_6635", "6918_6929", "8136_8145", "8419_8471", "8681_8702", "9223_9311", "9397_9512"]

for i, region in enumerate(regions):
	try:
		ene_val = []
		with open(ene_logs+"H77_"+region+"_energy.log") as f:
			for line in f.readlines():
				line = line.strip()
				ene_val.append(float(line))
				
		best_model = np.argmin(ene_val)  #Least energy structure is the best
		
		mlist = []
		for fname in os.listdir(inpath):
			if(fname.endswith(region)):
				mlist = [x for x in os.listdir(inpath+fname+"/output/models/") if x.endswith("_minim.pdb")]
				break
		
		os.system("cp "+inpath+fname+"/output/models/"+mlist[best_model]+" "+outpath)
		os.system("mv "+outpath+mlist[best_model]+" "+outpath+region+"_FARFAR2_best.pdb")
		print(region, best_model)
	except:
		continue


















