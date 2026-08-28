#Prepare input files for docking with a HETATM record in the COM of every binding site

import re
import sys
import csv
import pandas as pd
import numpy as np
import math

infile = sys.argv[1]
pdbpath = sys.argv[2]
outpath = sys.argv[3]

#---------------------------------------------------------------------------------------------------------------------------------------
#Function to extract atoms corresponding to a residue ID
def extract_atoms_from_resid(pdb_atoms, residue_id):
	atoms = []
	for atom in pdb_atoms:
		chain = atom[21:22]
		residue = atom[22:27].strip()
		resiname = atom[17:20].strip()
		resid = str(resiname)+"_"+str(residue)+"_"+str(chain)

		if(resid==residue_id):
			atoms.append(atom)

	return atoms

#Centroid extraction
def extract_centroid(atoms):
	centroid = []
	
	done = 0
	x_avg = 0.0
	y_avg = 0.0
	z_avg = 0.0
	for atom in atoms:
		coords = [float(atom[30:38].strip()), float(atom[38:46].strip()), float(atom[46:54].strip())]
		x_avg = x_avg + coords[0]
		y_avg = y_avg + coords[1]
		z_avg = z_avg + coords[2]
		done = done + 1
		
	centroid.append(np.round(x_avg/done, 3))
	centroid.append(np.round(y_avg/done, 3))
	centroid.append(np.round(z_avg/done, 3))
	
	return centroid
#---------------------------------------------------------------------------------------------------------------------------------------

df = pd.read_csv(infile, sep="\t", header=0)
#print(df.columns)  #['PDB_ID', 'PDB_map', 'Chain_ID', 'Binding_site_residues']

for i, row in df.iterrows():	
	pdb_atoms = []
	with open(pdbpath+row["PDB_map"]+"_FARFAR2_best.pdb") as f:
		for line in f.readlines():
			line = line.strip()
			if(line.startswith("ATOM")):
				pdb_atoms.append(line)
				
	out = open(outpath+row["PDB_ID"]+".pdb", "w")
	for atom in pdb_atoms:
		if(atom!="END"):
			print(atom, file=out)
	
	start = 10000
	resi_st = 700		
	
	bs_residues = row["Binding_site_residues"].split(",")
	atom_list = []
	for resi in bs_residues:
		atom_list.extend(extract_atoms_from_resid(pdb_atoms, resi))
	
	pocket_com = extract_centroid(atom_list)
	idx = "P"+str(row["PDB_ID"].split("_")[-1])
	
	template = "{:6s}{:5d} {:^4s}{:1s}{:3s} {:1s}{:4d}{:1s}   {:>8.3f}{:>8.3f}{:>8.3f}{:6.2f}{:6.2f}          {:>2s}{:2s}".format("HETATM",start,"MG"," ",idx,"A",resi_st," ",pocket_com[0],pocket_com[1],pocket_com[2],1.00,42.28,"MG"," ")
	
	print(template, file=out)	
	print("END", file=out)
	out.close()
	f.close()
	print(row["PDB_ID"])































