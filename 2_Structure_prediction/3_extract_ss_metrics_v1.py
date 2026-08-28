#Program to extract the best metrics for each HCV region

import os
import sys
import csv
import pandas as pd
import numpy as np

inpath = sys.argv[1]
outfile = sys.argv[2]

regions = ["49_114", "592_663", "762_816", "1010_1050", "1277_1293", "1320_1534", "2049_2117", "2287_2362", "2520_2561", "3293_3362", "3716_3799", "3864_3895", "4558_4671", "4873_4968", "5297_5411", "5444_5499", "5807_5876", "5999_6074", "6518_6635", "6918_6929", "8136_8145", "8419_8471", "8681_8702", "9223_9311", "9397_9512"]

out = open(outfile, "w")
print("Region\tBest_bp_dist\tModel_ID\tBest_energy\tModel_ID\tMean_bp_dist\tSD_bp_dist\tMean_energy\tSD_energy", file=out)

for i, reg in enumerate(regions):
	dist_val = []
	ene_val = []
	
	try:
		with open(inpath+"H77_"+reg+"_dist.log") as f1:
			for line in f1.readlines():
				line = line.strip()
				contents = line.split(": ")
				dist_val.append(int(contents[-1]))
		
		with open(inpath+"H77_"+reg+"_energy.log") as f2:
			for line in f2.readlines():
				line = line.strip()
				ene_val.append(float(line))
		
		best_ene = min(ene_val)
		ene_best = np.argmin(ene_val)
		best_dist = min(dist_val)
		if(dist_val[ene_best]==best_dist):
			dist_best = ene_best
		else:
			dist_best = np.argmin(dist_val)
			
		print(reg+"\t"+str(best_dist)+"\t"+str(dist_best+1)+"\t"+str(best_ene)+"\t"+str(ene_best+1)+"\t"+str(np.mean(dist_val))+"\t"+str(np.round(np.std(dist_val), 2))+"\t"+str(np.round(np.mean(ene_val), 2))+"\t"+str(np.round(np.std(ene_val),2)), file=out)
	except:
		print(reg+"\t-\t-\t-\t-\t-\t-\t-\t",file=out)

	#break






















