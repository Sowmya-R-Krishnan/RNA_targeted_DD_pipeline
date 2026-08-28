# A Novel <i>in silico</i> Method for RNA-Targeted Drug Design Against the Hepatitis C Virus
Authors: Sowmya Ramaswamy Krishnan, Arijit Roy*, Limsoon Wong, M. Michael Gromiha*

Module 1: Automation scripts used for RNA target identification module using RNAFramework, Infernal and R-scape packages. Requires 3 inputs:
 - Genomic sequence of a reference genotype/isolate (Ex: HCV genotype 1a)
 - Chemical probing dataset (SHAPE-MaP) for the isolate
 - A database of genomic sequences of all isolates/genotypes against which covariance modelling has to be performed (Ex: All 7 HCV genotypes)
 
Breaks are present in between the automated processes wherein manual analysis or error resolution was performed. The HCV SHAPE-MaP dataset used in this study is available from: https://doi.org/10.1073/pnas.1416266112

# Requirements - Preferably a conda environment with all these packages installed
* python>=v3.10.13
* pandas>=2.2.3
* numpy>=1.26.4

# Other additional stand-alone programs required (to be compiled as per each package installation instructions)
* RNAstructure - https://rna.urmc.rochester.edu/RNAstructure.html
* RNAFramework - https://github.com/dincarnato/RNAFramework
* cm-builder - https://github.com/dincarnato/labtools
* Infernal - https://github.com/EddyRivasLab/infernal
* R-scape - https://github.com/EddyRivasLab/R-scape

# Usage disclaimer
This is a minimal version of the pipeline source code necessary to reproduce the automated steps of the pipeline. Wherever possible, the manual resolution results are also provided. Any changes made to the source code (except paths to stand-alone programs) are done at your own risk. The authors will not be liable to any discrepancies observed in the results due to changes made by the user to the source code.

# Data
Sample input and output files and any data used from external databases are provided under the `data` directory.

# Code usage
For any queries related to code usage, contact the corresponding author for more information.

# Sample commands
1. RNA folding using RNAstructure with SHAPE reactivities as pseudo-energy constraints - `bash 1_run_RNAstructure_v1.sh`

2. Convert the .ct output file to DBN notation using the RNAstructure web server (https://rna.urmc.rochester.edu/RNAstructureWeb/Servers/ct2dot/ct2dot.html)

3. Extract median reactivity and entropy values from raw SHAPE-Map data for a sliding window of interest - `python 2_extract_median_values_v1.py data/H77_SHAPE_data_Weeks_2015.csv output/H77_median_values_50nt_v1.csv 50`

4. Extract .db files for low Shannon-low SHAPE regions using a median reactivity/entropy threshold - `python 3_extract_regions_of_interest_v2.py output/H77_median_values_50nt_v1.csv data/H77_1a_SS.txt output/Stable_regions/ 50 75`

5. Run RNAFramework (cm-builder) for covariance modelling and analysis using Infernal - `bash 4_run_cm_builder.sh`

# Miscellaneous
* Set the Fold program path in the shell script (`1_run_RNAstructure_v1.sh`) before using it
* Create output directories such as `Stable_regions` and `Infernal_results` before running scripts
* All scripts from the labtools package and R-scape need to be kept in the same directory as `4_run_cm_builder.sh` before using it
* A folder will be generated for each stable region identified from the SHAPE-MaP analysis by the cm-builder script
* Only the output files generated with HCV genotype 1 isolates have been provided in the `output` folder

# License: MIT License










