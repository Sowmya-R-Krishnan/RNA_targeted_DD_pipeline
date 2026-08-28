#Program to extract the secondary structures from PDB files and compare them

import os
import sys
import csv
import re
import pandas as pd
import numpy as np
import RNA
import subprocess

inpath = sys.argv[1]
prefix = sys.argv[2]
nmodels = sys.argv[3]
outpath = sys.argv[4]

regions = ["49_114", "592_663", "762_816", "1010_1050", "1277_1293", "1320_1534", "2049_2117", "2287_2362", "2520_2561", "3293_3362", "3716_3799", "3864_3895", "4558_4671", "4873_4968", "5297_5411", "5444_5499", "5807_5876", "5999_6074", "6518_6635", "6918_6929", "8136_8145", "8419_8471", "8681_8702", "9223_9311", "9397_9512"]

ref_ss = ["((((.....((((...(((.((...((((((.......))))))....)).)))....))))))))", "(((.....(((..(((((((((((((.(((((((......)))))))))).))))))))))))).....)))", "((((((((....)).)))))).(((((((((.(((((...))))).)))))))))", "((.(((((((..(((((((....)))))))..)))))))))", "(....(((....))).)", "(((((..(((..((((((((((((((.((((.(((((((((((((....((((((((((...(((((((.((((((.(((((....))))).)))))))))).)))..)))))))))).....)))).....)))).)).)))))))..))))).))))))))).((((.((....)).)))).))))))))....(((((((.....)))))))", "(..(((((.(((((((((((.......)))))).))))).))))).(((((((........))))))))", "((...(((((((...((((...(((.(((.(((.........))).))).)))...))))...)))))))....))", "(((((((....))))))).................(.....)", "(((((((.((.......)).))))))).((((....))))..................((((....))))", "((((.(((((((((.......)))).)))))...)))).............................((((((.....))))))", "((((((((((.(((....))).))))))))))", "(((((((((....(((((((...(((((((.......)))))))..((((......))))...((((..((((((((...))))))))))))...)))))))...)))))))))", "(((.((.(((((..(.(((((((.(((.((.....((((((((.((((.....)))).)).))))))..)))))))))..)))).))))))).)))", "((((((.((((((((((((((....)))))))).))))))((((((.(((((.((((((((((..(((((....))))))))))))))).))))).)))))).......))))))", "((....)).((((((((..((((..(((((((...))))))).)))).))))))))", "(((((((.((((..(((((..((..(((((((((...)))))))))..))..))))).)).)))))))))", "((((((((((((.(.((.(((.(((((((((((.(((...)))..))))))))))))))..)))))))))))))))", "((((((((((..(((((...(((((..((.(((((...((((((..(((.(((((.....))))))))...))))))....))))).))....))))).....)))))))))))))))", "(((......)))", "(((....)))", "((((((((((...(((..(((((....)))))...))).....))))))))))", "(((((............)))))", "(((.((((((((((((....))))))))).)))))).........(((((((((((((..........)))))))........))))))", "(((.......)))..........................................................................................((((.....))))"]

fnames = os.listdir(inpath)

nmodels = int(nmodels)
for i, reg in enumerate(regions):
	ss_list = []
	energy_list = []
	
	folder = ""
	for fname in fnames:
		if(fname.startswith(prefix) and fname.endswith("H77_"+reg)):
			folder = fname
			break
	
	if(os.path.exists(inpath+folder+"/output/models/")):
		ss_list.append(ref_ss[i])
		minim_idx = 1
		for fname in os.listdir(inpath+folder+"/output/models/"):
			if(fname.endswith("_minim.pdb")):  #TODO: Modify if not using for minimized structures alone
				#Using DSSR (X3DNA) to get the secondary structure dot-bracket notation
				out_var1 = subprocess.check_output("./x3dna-dssr --more -i="+inpath+folder+"/output/models/"+fname, shell=True, stderr=subprocess.STDOUT)
				with open("dssr-2ndstrs.dbn") as ss_f:
					next(ss_f)
					next(ss_f)
					for line in ss_f.readlines():
						line = line.strip()
						ss_list.append(line)
						
				os.system("rm dssr-*")		
				
				os.system("rasp-fd-1.0/bin/rasp_fd -e all -p "+inpath+folder+"/output/models/"+fname+" -o "+outpath+"tmp.out")
				with open(outpath+"tmp.out") as f:
					for line in f.readlines():
						line = line.strip()
						if(re.search("[0-9+-]{1,}\s+", line)):
							all_atom_energy = float(line.split("\t")[0])
							
				energy_list.append(all_atom_energy)
				os.system("rm "+outpath+"tmp.out")
				#break

	outfile1 = outpath+"H77_"+reg+"_SS_out.seq"
	outfile2 = outpath+"H77_"+reg+"_dist.log"
	outfile3 = outpath+"H77_"+reg+"_energy.log"
	out1 = open(outfile1, "w")
	out2 = open(outfile3, "w")
	for ss in ss_list:
		ss = ss.replace("[",".").replace("]",".")  #Removes pseudoknots from structure
		print(ss, file=out1)
		
	for ene in energy_list:	
		print(str(ene), file=out2)
		
	out1.close()
	out2.close()

	os.system("RNAdistance -Xf < "+outfile1+" > "+outfile2)
	
	print(reg)
	#break


























