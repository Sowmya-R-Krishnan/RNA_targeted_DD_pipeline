# A Novel <i>in silico</i> Method for RNA-Targeted Drug Design Against the Hepatitis C Virus
Authors: Sowmya Ramaswamy Krishnan, Arijit Roy*, Limsoon Wong, M. Michael Gromiha*

Module 3: Utility scripts for analysis of Target validation results. Requires predicted druggable binding sites for each stable region modelled in Module 2 using the DRLiPS program.

# Requirements - Preferably a conda environment with all these packages installed
* python>=v3.10.13
* pandas>=2.2.3
* numpy>=1.26.4
* biopython>=1.83

# Other additional stand-alone programs required (to be compiled as per each package installation instructions)
* DRLiPS - https://github.com/Sowmya-R-Krishnan/DRLiPS

# Usage disclaimer
This is a minimal version of the pipeline source code necessary to reproduce the automated steps of the pipeline. Wherever possible, the manual resolution results are also provided. Any changes made to the source code (except paths to stand-alone programs) are done at your own risk. The authors will not be liable to any discrepancies observed in the results due to changes made by the user to the source code.

# Data
Sample input and output files and any data used from external databases are provided under the `data` directory.

# Code usage
For any queries related to code usage, contact the corresponding author for more information.

# Sample commands
1. Analyze druggability predictions from DRLiPS for all FARFAR2 models and prepare consensus pocket clusters - `python 1_analyze_druggability_results_v1.py data/DRLiPS_raw/ output/DRLiPS_consensus_scores/`

2. Extract the PDB files with binding site residues predicted by DRLiPS - `python 2_extract_binding_sites_v1.py output/DRLiPS_consensus_scores/ ../2_Structure_prediction/output/Minimized_best/ output/Binding_sites/`

# Miscellaneous
* DRLiPS web server can also be used in "All Sites mode" to predict druggable binding sites for each stable region - https://web.iitm.ac.in/bioinfo2/DRLiPS/
* Create the `DRLiPS_consensus_scores` folder before running the analysis script (`1_analyze_druggability_results_v1.py`).
* Create the `Binding_sites` folder before running the PDB file extraction script (`2_extract_binding_sites_v1.py`).
* The scripts for RMscore computation against all PDB-derived binding sites is not included in the directory. The final set of binding sites used in this study were derived based on this analysis.

# License: MIT License










