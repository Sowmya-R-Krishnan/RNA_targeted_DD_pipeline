#Program to extract median Shannon entropies and SHAPE reactivities from a SHAPE dataset

import sys
import csv
import pandas as pd
import numpy as np
import statistics
from statistics import median

infile = sys.argv[1]
outfile = sys.argv[2]
window_size = sys.argv[3]

shape_df = pd.read_csv(infile, sep="\t", header=0)
#print(shape_df.columns)  #Index(['Position', 'Base', 'Reactivity', 'Shannon Entropy'], dtype='object')

window_size = int(window_size)+1
centre_left = int(window_size/2)
centre_right = int(window_size/2)

out = open(outfile, "w")
print("Position\tBase\tReactivity\tShannon_entropy\tMedian_reactivity\tMedian_entropy", file=out)

for i, row in shape_df.iterrows():
	if(i<centre_left):
		shape_median = ""
		shannon_median = ""
		print(str(row["Position"])+"\t"+row["Base"]+"\t"+str(row["Reactivity"])+"\t"+str(row["Shannon Entropy"])+"\t"+str(shape_median)+"\t"+str(shannon_median), file=out)

	else:
		pos_left = i - centre_left
		pos_right = i + centre_right
		if(pos_right+1>len(shape_df.index)):
			pos_right = len(shape_df.index)
		else:
			pos_right = pos_right + 1
		
		shape_vals = []
		shannon_vals = []
		for j in range(pos_left, pos_right):
			shape_vals.append(shape_df.loc[j]["Reactivity"])
			shannon_vals.append(shape_df.loc[j]["Shannon Entropy"])
			
		#print(i, centre_left, pos_left, pos_right, len(shape_vals), len(shannon_vals))  #X, X-25, X+25, 50, 50
		shape_median = median(shape_vals)
		shannon_median = median(shannon_vals)
		#print(shape_median, shannon_median)
		
		print(str(row["Position"])+"\t"+row["Base"]+"\t"+str(row["Reactivity"])+"\t"+str(row["Shannon Entropy"])+"\t"+str(shape_median)+"\t"+str(shannon_median), file=out)
		#break

print("Median values extracted for "+str(window_size)+" nt windows.")






























