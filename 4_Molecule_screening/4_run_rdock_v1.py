#Program to run RxDock calculations for the RNA library against HCV

import os
import sys
import csv
import pandas as pd
import numpy as np
import subprocess

param_path = sys.argv[1]
lig_path = sys.argv[2]
outpath = sys.argv[3]

ligands = os.listdir(lig_path)
done = []

for receptor in os.listdir(param_path):
	fname = receptor.replace("_rdock.prm", "")
	
	if(fname not in done):
		os.system("mkdir "+outpath+fname)

		for i, lig in enumerate(ligands):
			#print(receptor, lig)
			try:	
				#os.system("export RBT_ROOT=/home/sowmya/Downloads/rDock_2013.1_src/")
				out_var1 = subprocess.check_output("rbcavity -W -d -r "+param_path+receptor, shell=True)
				out_var2 = subprocess.check_output("timeout 60s rbdock -i "+lig_path+lig+" -o "+outpath+fname+"/"+fname+"_"+lig.replace(".sdf","")+"_out -r "+param_path+receptor+" -p ./dock_solv.prm -n 1 -s 123456", shell=True)
			except:
				continue
				
		print(fname+" Done.")
		#break
	else:
		print(fname+" Done.")




























