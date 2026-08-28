#Program to extract regions of interest from a SHAPE dataset

import sys
import csv
import pandas as pd
import numpy as np
import statistics
import itertools
from statistics import median
from collections import Counter

infile = sys.argv[1]
dotbracket = sys.argv[2]
outpath = sys.argv[3]
window_size = sys.argv[4]
threshold = sys.argv[5]  #Between 0 and 1 (0% - 100%)

shape_df = pd.read_csv(infile, sep="\t", header=0)
#print(shape_df.columns)  #['Position', 'Base', 'Reactivity', 'Shannon_entropy', 'Median_reactivity', 'Median_entropy']

global_reactivity_median = median(list(shape_df["Reactivity"]))
global_entropy_median = median(list(shape_df["Shannon_entropy"]))

print("Global SHAPE median: "+str(global_reactivity_median))
print("Global Shannon median: "+str(global_entropy_median))

window_size = int(window_size)
threshold = float(threshold)

#------------------------------------------------------Low Shannon - Low SHAPE regions-----------------------------------------------------
pass_shape_entropy = []
for i, row in shape_df.iterrows():
	if(pd.isna(row["Median_reactivity"])):
		pass_shape_entropy.append(0)
	elif((row["Median_reactivity"] < global_reactivity_median) and (row["Median_entropy"] < global_entropy_median)):
		pass_shape_entropy.append(1)
	else:
		pass_shape_entropy.append(0)

pass_regions = []
for i in range(0, len(pass_shape_entropy)):
	try:
		sub_pass = pass_shape_entropy[i:i+window_size]
	except:
		sub_pass = pass_shape_entropy[i:]

	if((sum(sub_pass)/window_size) >= threshold):
		pass_regions.append((i, i+window_size))

base_list = list(shape_df["Base"])	
		
final_regions = [range(x[0], x[1]) for x in pass_regions]
pass_bases = []
for r in final_regions:
	expand = np.r_[r].tolist()
	pass_bases.extend(expand)
	
pass_bases = list(set(pass_bases))
pass_bases.sort()

groups = (list(x) for _, x in itertools.groupby(pass_bases, lambda x, c=itertools.count(): x - next(c)))
reg_str = ', '.join('-'.join(map(str, (item[0], item[-1]+1)[:len(item)])) for item in groups)
stable_regions = reg_str.split(", ")
print("No. of Low Shannon - Low SHAPE regions in "+str(window_size)+" nt window: "+str(len(stable_regions)))

#------------------------------------------------------------------SS CHECK----------------------------------------------------------------
#Function to check if secondary structures are fully formed and truncate regions which are incomplete base-pairs
def ss_check(start, end, seq, ss):
	new_start = start
	new_end = end
	new_seq = ""
	new_ss = ""
	
	ss_counts = Counter(ss)
	if(ss_counts["("]==ss_counts[")"]):
		return start, end, seq, ss
	else:
		starts = []
		ends = []
		bp_stack = []
		stranded = []
		for j, char in enumerate(ss):
			if(char=="("):
				bp_stack.append(j)
			try:
				if(char==")"):
					id1 = bp_stack.pop()
					id2 = j	
					starts.append(id1)
					ends.append(id2)
			except:
				stranded.append(j)
				
		trim_sites = []
		if(len(bp_stack)>0):
			trim_sites.extend(bp_stack)
		if(len(stranded)>0):
			trim_sites.extend(stranded)
			
		starts = sorted(starts)
		ends = sorted(ends)
		trim_sites = sorted(trim_sites)
		
		ss_repl = ""
		for i, ch in enumerate(list(ss)):
			if(i in trim_sites):
				ss_repl = ss_repl+"."
			else:
				ss_repl = ss_repl+ch
		
		new_start = start + starts[0]
		new_end = start + ends[-1]
		new_seq = seq[starts[0]:ends[-1]+1]
		new_ss = ss_repl[starts[0]:ends[-1]+1]
		
		return new_start, new_end, new_seq, new_ss
	

ss_dot = ""
with open(dotbracket) as ss:
	for line in ss.readlines():
		line = line.strip()
		if(line.startswith(".") or line.startswith("(")):
			ss_dot = line

revised_stable = []
for region in stable_regions:
	start = int(region.split("-")[0])
	end = int(region.split("-")[1])
	
	seq = "".join(base_list[start-1:end])
	ss = ss_dot[start-1:end]
	
	try:
		rstart, rend, rseq, rss = ss_check(start, end, seq, ss)
		revised_stable.append((rstart, rend))
		print(">H77 region "+str(rstart)+"-"+str(rend))
		print(rseq)
		print(rss)
		print("")
		
		out = open(outpath+"H77_region_"+str(rstart)+"_"+str(rend)+".db", "w")
		print(">H77 region "+str(rstart)+"-"+str(rend), file=out)
		print(rseq, file=out)
		print(rss, file=out)
		out.close()
	except:
		continue

print(revised_stable)













