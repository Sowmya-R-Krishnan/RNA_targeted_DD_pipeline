#Analyze interaction results from fingeRNAt for each binding site

import os
import sys
import csv
import pandas as pd
import numpy as np
from collections import Counter, defaultdict

inpath = sys.argv[1]
outpath = sys.argv[2]

gout = open("General_interaction_analysis_results_v1.csv", "w")
print("RNA_target\tHB\tHAL\tPi_Anion\tPi_Stacking\tLipophilic\tResi_count", file=gout)

for fname in os.listdir(inpath):
	if(fname.startswith("DETAIL_")):
		target = fname.split(".")[0].replace("DETAIL_","")	
	
		df = pd.read_csv(inpath+fname, sep="\t", header=0)
		#print(df.columns)  #['Unnamed: 0', 'Ligand_name', 'Ligand_pose', 'Ligand_occurrence_in_sdf', 'Interaction', 'Ligand_Atom', 'Ligand_X', 'Ligand_Y', 'Ligand_Z', 'Receptor_Residue_Name', 'Receptor_Number', 'Receptor_Chain', 'Receptor_Atom', 'Receptor_X', 'Receptor_Y', 'Receptor_Z', 'Distance']
		
		out = open(outpath+target+"_ints_final_v1.csv", "w")
		print("Ligand_name\tHB\tHAL\tPi_Anion\tPi_Stacking\tLipophilic\tResi_count", file=out)
		
		resi_all = []
		for n in range(100):
			sub_df = df[df["Ligand_occurrence_in_sdf"]==n+1]
			resi_list = defaultdict(list)
			resi_list = {"HB":[], "Lipophilic":[], "Pi_Anion":[], "Pi_Stacking":[], "HAL":[]}
			unique_resi = []
			for j, row in sub_df.iterrows():
				resi_id = row["Receptor_Residue_Name"]+"_"+str(row["Receptor_Number"])+"_"+str(row["Receptor_Chain"])
				if(resi_id not in resi_list[row["Interaction"]]):
					resi_list[row["Interaction"]].append(resi_id)
				if(resi_id not in unique_resi):
					unique_resi.append(resi_id)
				if(resi_id not in resi_all):
					resi_all.append(resi_id)
				#print(resi_id, row["Interaction"])
				
			print(row["Ligand_name"]+"\t"+",".join(resi_list["HB"])+"\t"+",".join(resi_list["HAL"])+"\t"+",".join(resi_list["Pi_Anion"])+"\t"+",".join(resi_list["Pi_Stacking"])+"\t"+",".join(resi_list["Lipophilic"])+"\t"+str(len(unique_resi)), file=out)
		out.close()
		
		new_df = pd.read_csv(outpath+target+"_ints_final_v1.csv", sep="\t", header=0)
		new_df.fillna('-', inplace=True)
		new_df.to_csv(outpath+target+"_ints_final_v1.csv", sep="\t", header=True, index=False)
		
		out = open(outpath+target+"_resi_importance_v1.csv", "w")
		print("Binding_site_residue\tHB\tHAL\tPi_Anion\tPi_Stacking\tLipophilic\tTotal", file=out)
		
		for resi in resi_all:
			hb = 0
			hal = 0
			pi_anion = 0
			pi_stacking = 0
			lipo = 0
			total = 0
			found = False
			for i, row in new_df.iterrows():
				if(row["HB"]!="-" and resi in row["HB"].split(",")):
					hb = hb + 1
					found = True
				if(row["HAL"]!="-" and resi in row["HAL"].split(",")):
					hal = hal + 1
					found = True
				if(row["Pi_Anion"]!="-" and resi in row["Pi_Anion"].split(",")):
					pi_anion = pi_anion + 1
					found = True
				if(row["Pi_Stacking"]!="-" and resi in row["Pi_Stacking"].split(",")):
					pi_stacking = pi_stacking + 1
					found = True
				if(row["Lipophilic"]!="-" and resi in row["Lipophilic"].split(",")):
					lipo = lipo + 1
					found = True
				if(found==True):
					total = total + 1
					
			print(resi+"\t"+str(hb/100)+"\t"+str(hal/100)+"\t"+str(pi_anion/100)+"\t"+str(pi_stacking/100)+"\t"+str(lipo/100)+"\t"+str(total/100), file=out)
			
		#break
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
