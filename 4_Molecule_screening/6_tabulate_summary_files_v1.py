#Program to tabulate summary files of all docking calculations to compare the results across ligands

import os
import sys
import csv
import pandas as pd
import numpy as np

inpath = sys.argv[1]
lig_file = sys.argv[2]
outfile = sys.argv[3]

lig_df = pd.read_csv(lig_file, sep="\t", header=0)

out = open(outfile, "w")
print("Receptor\tLigand\tSMILES\tTotal_score\tInter_score\tIntra_score\tSystem_score\tNormalized_score", file=out)

for summary in os.listdir(inpath):
	name = summary.replace("_out.log","").split("_")
	receptor = "_".join(name[0:3])
	ligand = "_".join(name[3:])
	smiles = lig_df[lig_df["Mol_ID"]==ligand]

	scores = {"SCORE":"---", "SCORE.INTER":"---", "SCORE.INTRA":"---", "SCORE.SYSTEM":"---", "SCORE.norm":"---"}
	with open(inpath+summary) as f:
		for line in f.readlines():
			line = line.strip()
			if(line.startswith("SCORE ")):
				contents = line.split(" ")
				scores["SCORE"] = contents[-1].strip()
			elif(line.startswith("SCORE.INTER ")):
				contents = line.split(" ")
				scores["SCORE.INTER"] = contents[-1].strip()
			elif(line.startswith("SCORE.INTRA ")):
				contents = line.split(" ")
				scores["SCORE.INTRA"] = contents[-1].strip()
			elif(line.startswith("SCORE.SYSTEM ")):
				contents = line.split(" ")
				scores["SCORE.SYSTEM"] = contents[-1].strip()
			elif(line.startswith("SCORE.norm ")):
				contents = line.split(" ")
				scores["SCORE.norm"] = contents[-1].strip()
				
	#print(receptor, ligand, scores)
	print(receptor+"\t"+str(ligand)+"\t"+smiles.iloc[0]["Unique_SMILES"]+"\t"+scores['SCORE']+"\t"+scores['SCORE.INTER']+"\t"+scores['SCORE.INTRA']+"\t"+scores['SCORE.SYSTEM']+"\t"+scores['SCORE.norm'], file=out)

	#break





























