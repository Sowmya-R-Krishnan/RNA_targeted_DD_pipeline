#Program to obtain the result summaries for all docking outputs from RxDock

import os
import sys
import csv
import pandas as pd
import numpy as np

inpath = sys.argv[1]
outpath = sys.argv[2]

os.system("mkdir "+outpath+inpath.replace("output/Sample_results/",""))

for sdfile in os.listdir(inpath):
	os.system("sdreport -s "+inpath+sdfile+" >> "+outpath+inpath.replace("output/Sample_results/","")+sdfile.replace(".sd", ".log"))

print("Done.")




























