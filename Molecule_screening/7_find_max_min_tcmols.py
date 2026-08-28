#Compare two datasets to find out novel scaffolds and enumerate them

import sys
import csv
import pandas as pd
import numpy as np
import pickle
from matplotlib import pyplot as plt
from rdkit import Chem
from rdkit import DataStructs
from rdkit.Chem.Fingerprints import FingerprintMols
from rdkit.Chem import Scaffolds
from rdkit.Chem import Draw, Descriptors
from rdkit.Chem.Scaffolds import MurckoScaffold
import seaborn as sns

data1 = sys.argv[1]
data2 = sys.argv[2]
outfile = sys.argv[3]

expt_ligands = []
expt_molname = []
other_ligands = []
other_ligands_id = []

df1 = pd.read_csv(data1, sep="\t", header=0)
expt_ligands = list(df1["Unique_SMILES"])
expt_molname = list(df1["Mol_ID"])

print("Dataset 1 read!")

df2 = pd.read_excel(data2, header=0)
other_ligands = list(df2["SMILES"])
other_ligands_id = list(df2["Mol_ID"])

print("Dataset 2 read!")

fp1_list = []
mol1_fpval = []
for n,mol1 in enumerate(expt_ligands):
	try:
		mol1 = Chem.MolFromSmiles(mol1)
		fp1_list.append(FingerprintMols.FingerprintMol(mol1))
		mol1_fpval.append(expt_ligands[n])
	except:
		continue

fp2_list = []
mol2_fpval = []
mol2_fpval_id = []
for n,mol2 in enumerate(other_ligands):
	try:
		mol2 = Chem.MolFromSmiles(mol2)
		fp2_list.append(FingerprintMols.FingerprintMol(mol2))
		mol2_fpval.append(other_ligands[n])
		mol2_fpval_id.append(other_ligands_id[n])
	except:
		continue

def tanimotocalc(fp1,fp2list):
	tanimoto_values = []
	tanimoto_values = [DataStructs.FingerprintSimilarity(fp1, fp2, metric=DataStructs.TanimotoSimilarity) for fp2 in fp2list]
	return tanimoto_values

maxtcmol = []
maxtcval = []
mintcmol = []
mintcval = []
for j,fp1 in enumerate(fp1_list):
	tanimoto_val = []
	tanimoto_val = tanimotocalc(fp1,fp2_list)
	maxtcmol.append(tanimoto_val.index(max(tanimoto_val)))
	maxtcval.append(max(tanimoto_val))

for j,fp1 in enumerate(fp1_list):
	tanimoto_val = []
	tanimoto_val = tanimotocalc(fp1,fp2_list)
	mintcmol.append(tanimoto_val.index(min(tanimoto_val)))
	mintcval.append(min(tanimoto_val))

with open(outfile, 'w') as f:
	for i,mol1 in enumerate(mol1_fpval):
		print(mol1+"\t"+str(mol2_fpval[maxtcmol[i]])+"\t"+str(maxtcval[i])+"\t"+str(mol2_fpval_id[maxtcmol[i]]), file=f)
	








