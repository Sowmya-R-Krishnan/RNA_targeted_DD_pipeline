# A Novel <i>in silico</i> Method for RNA-Targeted Drug Design Against the Hepatitis C Virus
Authors: Sowmya Ramaswamy Krishnan, Arijit Roy*, Limsoon Wong, M. Michael Gromiha*

Module 2: Utility scripts for analysis of Structure prediction results. Requires structures predicted using FARFAR2 web server for each stable region identified in Module 1.

# Requirements - Preferably a conda environment with all these packages installed
* python>=v3.10.13
* pandas>=2.2.3
* numpy>=1.26.4
* ViennaRNA

# Other additional stand-alone programs required (to be compiled as per each package installation instructions)
* X3DNA (DSSR) - https://x3dna.org/
* RNA-align - https://zhanggroup.org/RNA-align/download.html
* QRNAS - https://genesilico.pl/software/stand-alone/qrnas
* RASP - http://melolab.org/webrasp/download.php

# Usage disclaimer
This is a minimal version of the pipeline source code necessary to reproduce the automated steps of the pipeline. Wherever possible, the manual resolution results are also provided. Any changes made to the source code (except paths to stand-alone programs) are done at your own risk. The authors will not be liable to any discrepancies observed in the results due to changes made by the user to the source code.

# Data
Sample input and output files and any data used from external databases are provided under the `data` directory.

# Code usage
For any queries related to code usage, contact the corresponding author for more information.

# Sample commands
1. Use the FARFAR2 web server to predict 3D structure for each stable region from Module 1 - https://rosie.rosettacommons.org/farfar2

2. Energy minimization with QRNAS program - `python 1_run_minimization_v1.py data/`

3. Comparison of predicted secondary structures with SHAPE-derived structures for all FARFAR2 models after minimization - `python 2_compare_FARFAR2_ss_v1.py data/ rosie.farfar2.121547.H77_ 10 output/SS_comp_results/`

4. Extract the best SS and energy values (RASP) obtained for each stable region - `python 3_extract_ss_metrics_v1.py output/SS_comp_results/ output/FARFAR2_minim_SS_metrics_v1.csv`

5. Extract the best model for each stable region - `python 4_copy_best_models_v1.py data/ output/SS_comp_results/ output/Minimized_best/`

# Miscellaneous
* The predicted structures from FARFAR2 web server for one example stable region is provided under the `data` folder due to size limits. For more details on benchmarking of 7 different RNA tertiary structure prediction methods to arrive at FARFAR2, please refer to our article.
* Place the `QRNAS` package files in the same directory as the minimization script (`1_run_minimization_v1.py`).
* Create the `SS_comp_results` directory before running the comparison script (`2_compare_FARFAR2_ss_v1.py`).
* Create the `Minimized_best` directory before running the best model extraction script (`4_copy_best_models_v1.py`).

# License: MIT License










