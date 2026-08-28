#Program to extract binding sites given a residue list using BioPython

import os
import sys
import csv
import pandas as pd
import numpy as np
from Bio import PDB
from Bio.PDB import PDBParser, PDBIO, Select, NeighborSearch
import warnings

inpath = sys.argv[1]
pdbpath = sys.argv[2]
outpath = sys.argv[3]

#Atom selection class
class ResidueSelect(Select):
	def __init__(self, accepted_resi, omit_resi, model_id):
		self.accepted_resi = accepted_resi
		self.omit_resi = omit_resi
		self.model_id = model_id
		self.ions = ['H_NCO', 'H_NA', 'H_RHD', 'H_SR', 'H_PO4', 'H_ZN', 'H_MG', 'H_AG', 'H_K', 'H_AU3', 'H_NI', 'H_SE4', 'H_ACT', 'H_IRI', 'H_IR', 'H_CL', 'H_LU', 'H_TB', 'H_CA', 'H_CS', 'H_TL', 'H_SO4', 'H_CU', 'H_CAC', 'H_AU', 'H_BR', 'H_SM', 'H_CD', 'H_MN', 'H_NH4', 'H_IR3', 'H_CO', 'H_HG', 'H_3CO', 'H_OS', 'H_CON', 'H_BA', 'H_FE2', 'H_PB', 'H_SIN', 'H_MES', 'H_GOL', 'H_MPD', 'H_RU', 'H_NME', 'H_IOD', 'H_F', 'H_PT4', 'H_RB']

	def accept_residue(self, resi):
		#print(atom.full_id)  #('6tf3', 0, 'A', ('H_3AT', 109, ' '), ('PB', ' '))
		if(resi in self.accepted_resi and resi not in self.omit_resi and resi.full_id[1]==self.model_id and resi.resname!="HOH"):
			pass_c = 0
			pass_non_ion = 1
			if(resi.id[0].startswith("H_") and resi.id[0] not in self.ions):  #Removes any heteroatom records apart from ions
				pass_non_ion = 0
			
			for oresi in self.omit_resi:
				if(oresi.id[0]!=resi.id[0]):
					pass_c = pass_c + 1
					
			if(pass_c==len(self.omit_resi) and pass_non_ion==1):
				return 1
		else:
			return 0
			
ions = ['H_NCO', 'H_NA', 'H_RHD', 'H_SR', 'H_PO4', 'H_ZN', 'H_MG', 'H_AG', 'H_K', 'H_AU3', 'H_NI', 'H_SE4', 'H_ACT', 'H_IRI', 'H_IR', 'H_CL', 'H_LU', 'H_TB', 'H_CA', 'H_CS', 'H_TL', 'H_SO4', 'H_CU', 'H_CAC', 'H_AU', 'H_BR', 'H_SM', 'H_CD', 'H_MN', 'H_NH4', 'H_IR3', 'H_CO', 'H_HG', 'H_3CO', 'H_OS', 'H_CON', 'H_BA', 'H_FE2', 'H_PB', 'H_SIN', 'H_MES', 'H_GOL', 'H_MPD', 'H_RU', 'H_NME', 'H_IOD', 'H_F', 'H_PT4', 'H_RB']

for fname in os.listdir(inpath):
	if(fname.endswith("_consensus_scores_v1.csv")):
		reg = fname.replace("_consensus_scores_v1.csv", "")
		df = pd.read_csv(inpath+fname, sep="\t", header=0)
		
		for i, row in df.iterrows():
			bs_resi = row["Pocket residues"].split(", ")
			with warnings.catch_warnings():
				warnings.simplefilter('ignore')
				pdb_id = reg
				pdb = PDBParser().get_structure(pdb_id, pdbpath+pdb_id+"_FARFAR2_best.pdb")
				io = PDBIO()
				io.set_structure(pdb)
				
				sel_resi = []
				for model in pdb:
					for chain in model:
						for resi in chain:
							resid = resi.get_resname()+"_"+str(resi.id[1])+"_"+str(chain.id)
							if(resid in bs_resi):
								sel_resi.append(resi)
				
				io.set_structure(pdb)
				io.save(outpath+pdb_id+"_"+str(i+1)+".pdb", ResidueSelect(sel_resi, [], model.id))
			
		print(reg)





























