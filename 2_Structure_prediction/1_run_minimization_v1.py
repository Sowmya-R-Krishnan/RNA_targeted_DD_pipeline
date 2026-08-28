#Program to extract the secondary structures from PDB files and compare them

import os
import sys
import csv
import re
import pandas as pd
import numpy as np

inpath = sys.argv[1]

if(os.path.exists(inpath+"/output/models/")):
	for fname in os.listdir(inpath+"/output/models/"):
		os.system("../QRNAS-master/QRNA -i "+inpath+"/output/models/"+fname+" -o "+inpath+"/output/models/"+fname.replace(".pdb","_minim.pdb")+" -c ../QRNAS-master/configfile.txt")



























