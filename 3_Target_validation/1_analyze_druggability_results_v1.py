#Program to analyze the druggability prediction results for HCV stable regions

import os
import sys
import csv
import pandas as pd
import numpy as np
from itertools import combinations
from collections import defaultdict

inpath = sys.argv[1]
outpath = sys.argv[2]

fnames = os.listdir(inpath)
regions = ["49_114", "592_663", "762_816", "1010_1050", "1277_1293", "1320_1534", "2049_2117", "2287_2362", "2520_2561", "3293_3362", "3716_3799", "3864_3895", "4558_4671", "4873_4968", "5297_5411", "5444_5499", "5807_5876", "5999_6074", "6518_6635", "6918_6929", "8136_8145", "8419_8471", "8681_8702", "9223_9311", "9397_9512"]

for i, reg in enumerate(regions):
	results = [x for x in fnames if x.startswith(reg)]
	#print(results)
	
	pockets = {}
	scores = {}
	ranks = {}
	for fname in results:
		df = pd.read_csv(inpath+fname, sep="\t", header=0)
		df.sort_values("DRLiPS Druggability score", ascending=False, inplace=True)
		#print(df.columns)  #['Pocket ID', 'Pocket residues', 'DRLiPS Druggability score']
		for j, row in df.iterrows():
			pocket_resi = row["Pocket residues"].split(",")
			pocket_resi = [x.strip() for x in pocket_resi]
			pockets[row["Pocket ID"]] = pocket_resi
			scores[row["Pocket ID"]] = row["DRLiPS Druggability score"]
			ranks[row["Pocket ID"]] = j+1
			
	#print(pockets)
	pocket_pairs = set(list(combinations(list(pockets.keys()), 2)))
	overlap = {}
	unique_pockets = []
	for p1, p2 in pocket_pairs:
		l1 = pockets[p1]
		l2 = pockets[p2]
		common_resi = list(set(l1).intersection(set(l2)))
		percent = len(common_resi)/max(len(l1), len(l2))
		#print(p1, p2, percent)
		if(percent >= 0.7):
			overlap[(p1, p2)] = percent
			if(p1 not in unique_pockets):
				unique_pockets.append(p1)
			if(p2 not in unique_pockets):
				unique_pockets.append(p2)
	
	#print(unique_pockets)
	
	pocket_clusters = defaultdict(list)
	pockets_covered = []
	for p in unique_pockets:
		if(p not in pockets_covered):
			pockets_covered.append(p)
			for pair, val in overlap.items():
				if(pair[0]==p and pair[1] not in pockets_covered):
					pocket_clusters[p].append(pair[1])
					pockets_covered.append(pair[1])
				elif(pair[1]==p and pair[0] not in pockets_covered):
					pocket_clusters[p].append(pair[0])
					pockets_covered.append(pair[0])
				else:	
					continue
	#print(pocket_clusters)
	
	consensus_sites = {}
	consensus_scores = {}
	individual_ranks = {}
	for j, cluster in enumerate(list(pocket_clusters.keys())):
		cluster_p = [cluster]
		cluster_p.extend(pocket_clusters[cluster])
		c_resi = []
		c_scores = []
		rankval = []
		for p in cluster_p:
			c_scores.append(scores[p])
			rankval.append(ranks[p])
			for resi in pockets[p]:
				if(resi not in c_resi):
					c_resi.append(resi)
					
		consensus_sites["Site "+str(j+1)] = c_resi
		#print(cluster, c_scores)
		consensus_scores["Site "+str(j+1)] = np.round(np.mean(c_scores), 5)
		#print(rankval)
		
	#print(consensus_sites)
	#print(consensus_scores)	
	scores_sorted = {k: v for k, v in sorted(consensus_scores.items(), key=lambda item: item[1], reverse=True)}
	#print(scores_sorted)
	
	with open(outpath+reg+"_consensus_scores_v1.csv", "w") as out:
		print("Pocket_ID\tPocket_residues\tConsensus_DRLiPS_score", file=out)
		for key, val in scores_sorted.items():
			print(key+"\t"+",".join(consensus_sites[key])+"\t"+str(val), file=out)
		
	print(reg)
	#break




























