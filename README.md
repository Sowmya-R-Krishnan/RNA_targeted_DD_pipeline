# A Novel <i>in silico</i> Method for RNA-Targeted Drug Design Against the Hepatitis C Virus
Authors: Sowmya Ramaswamy Krishnan, Arijit Roy*, Limsoon Wong, M. Michael Gromiha*

Automation scripts for implementation of a computational pipeline for RNA-targeted drug discovery. Breaks are present in between the automated processes wherein manual predictions, analysis or error resolution was performed. All examples provided are related to Hepatitis C virus, but the pipeline is generic and can be repurposed for any organism with RNA genome and a SHAPE-MaP dataset.

# Requirements - Preferably a conda environment with all these packages installed
* python>=v3.10.13
* pandas>=2.2.3
* numpy>=1.26.4
* matplotlib
* seaborn
* rdkit-pypi>=2023.9.6
* openbabel==3.1.1
* biopython>=1.83

# Other additional stand-alone programs required (to be compiled as per each package installation instructions)
* RNAstructure - https://rna.urmc.rochester.edu/RNAstructure.html
* RNAFramework - https://github.com/dincarnato/RNAFramework
* cm-builder - https://github.com/dincarnato/labtools
* Infernal - https://github.com/EddyRivasLab/infernal
* R-scape - https://github.com/EddyRivasLab/R-scape
* X3DNA (DSSR) - https://x3dna.org/
* RNA-align - https://zhanggroup.org/RNA-align/download.html
* QRNAS - https://genesilico.pl/software/stand-alone/qrnas
* RASP - http://melolab.org/webrasp/download.php
* DRLiPS - https://github.com/Sowmya-R-Krishnan/DRLiPS
* RSAPred - https://github.com/Sowmya-R-Krishnan/RSAPred/
* PyMOL - https://www.pymol.org/
* rDock - https://rxdock.gitlab.io/
* fingeRNAt - https://github.com/n-szulc/fingeRNAt

# Usage disclaimer
This is a minimal version of the pipeline source code necessary to reproduce the automated steps of the pipeline. Wherever possible, the manual resolution results are also provided. Any changes made to the source code (except paths to stand-alone programs) are done at your own risk. The authors will not be liable to any discrepancies observed in the results due to changes made by the user to the source code.

# Data
Sample input and output files and any data used from external databases are provided under the `data` and `output` directories for each module.

# Code usage
Each module has a specific README.md file with instructions of usage. For any further queries related to code usage, contact the corresponding author for more information.

# Order of navigation
1. Target identification
2. Structure prediction
3. Target validation
4. Molecule screening

# Contact Us
For further queries related to code usage, please write to us: roy.arijit3@tcs.com & gromiha@iitm.ac.in

# Citation
Please cite our article if you have used the codes in this repository for your research: 

# License: MIT License










