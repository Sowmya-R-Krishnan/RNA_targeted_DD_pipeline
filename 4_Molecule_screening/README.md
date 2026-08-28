# A Novel <i>in silico</i> Method for RNA-Targeted Drug Design Against the Hepatitis C Virus
Authors: Sowmya Ramaswamy Krishnan, Arijit Roy*, Limsoon Wong, M. Michael Gromiha*

Module 4: Automation scripts to run virtual screening calculations with rDock and analysis of screening results to identify the best potential inhibitors for a given RNA region.

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
* RSAPred - https://github.com/Sowmya-R-Krishnan/RSAPred/
* PyMOL - https://www.pymol.org/
* rDock - https://rxdock.gitlab.io/
* fingeRNAt - https://github.com/n-szulc/fingeRNAt

# Usage disclaimer
This is a minimal version of the pipeline source code necessary to reproduce the automated steps of the pipeline. Wherever possible, the manual resolution results are also provided. Any changes made to the source code (except paths to stand-alone programs) are done at your own risk. The authors will not be liable to any discrepancies observed in the results due to changes made by the user to the source code.

# Data
Sample input and output files and any data used from external databases are provided under the `data` directory.

# Code usage
For any queries related to code usage, contact the corresponding author for more information.

# Sample commands
1. Generate the 3D SDF files with explicit hydrogens for the virtual screening library - `python 1_generate_mol_files.py data/RNA_VS_library_final.csv output/Sample_SDF/`

2. Prepare input pockets for docking by adding dummy Mg2+ ions at pocket centroid - `python 2_prepare_input_pockets_v1.py data/FARFAR2_sites_selected_v1.csv ../2_Structure_prediction/output/Minimized_best/ output/Docking_ready/`

3. Use PyMOL to separate the dummy atoms as reference ligands (`*_orig.sdf`) and receptor as MOL2 with explicit hydrogens (`*_receptor.mol2`). Save the files under `Receptors` directory for docking.

4. Prepare parameter files for rDock calculations - `python 3_prepare_rdock_prm_files_v1.py output/Receptors/ output/Parameter_files/`

5. Run rDock calculations - `python 4_run_rdock_v1.py output/Receptors/ output/Sample_SDF/ output/Sample_results/`

6. Get docking score summary files from rDock results (SDF files) - `python 5_get_vs_summary_v1.py output/Sample_results/592_663_3/ output/Sample_summary_files/`

7. Create a structured summary file from rDock logs - `python 6_tabulate_summary_files_v1.py output/Sample_summary_files/ output/Summary_tables/`

8. Check similarity between the virtual screening library and existing HCV RNA-targeting inhibitors or DrugBank dataset - `python 7_find_max_min_tcmols.py data/RNA_VS_library_final.csv data/HCV_validation_set_v1.xlsx output/RNA_dataset_vs_HCV_valset_maxTC_v1.csv`

9. Predict binding affinity (pKd) values for RNA-small molecule pairs using RSAPred and combine the similarity and affinity scores into a single CSV file per binding site (All final files provided in `output/Summary_tables` folder).

10. Select top-K molecules for each binding site for further interaction analysis. The filters used here are entirely user-defined. The top 100 molecules chosen in our study are provided in `output/Top_molecules` folder.

10. Prepare input files for interaction analysis with fingeRNAt package - `python 8_prepare_fingernat_input_sdf_v1.py output/Top_molecules/ output/Sample_results/ output/fingeRNAt_input/`

11. Run fingeRNAt calculations on the top molecules - `python 9_run_fingernat_v1.py output/fingeRNAt_input/ output/Docking_ready/`

12. Extract different types of interactions between top molecules and the binding site - `python 10_analyze_fingernat_output_v1.py output/fingeRNAt_output/ output/Interaction_analysis/`

13. Further analysis can be performed based on user's preferences. Identification of inhibitors with novel scaffolds was the goal in our study and Murcko Scaffolds in RDKit were used to do the analysis (Script not included in the repo).

# Miscellaneous
* RSAPred web server can also be used with the "Viral RNA - Generic model" to predict binding affinity values for RNA-small molecule pairs - https://web.iitm.ac.in/bioinfo2/RSAPred/
* OpenBabel can be used to interconvert between various molecular formats (SDF, MOL2, PDB, PDBQT, CIF etc)
* Only a sample of 10 SDF files from the virtual screening library is provided in the `output/Sample_SDF/` folder due to size constraints.
* Create the `Docking_ready` and `Receptors` folder before running the pocket preparation script (`2_prepare_input_pockets_v1.py`).
* Create the `Parameter_files` folder before running the parameter preparation script (`3_prepare_rdock_prm_files_v1.py`). Also set the complete path to receptor and reference ligand files in the script before proceeding further.
* Only a sample of the rDock output files are provided in the `Sample_results` directory. A total of 0.6 million output files will be generated which can lead to space constraints in user system. Please run `4_run_rdock_v1.py` at your own discretion.
* The environment variable `RBT_ROOT` must be set to point to the rDock installation directory before running docking calculations.
* Please ensure that the `dock_solv.prm` file is also placed in the directory before running rDock.
* Create `Sample_summary_files` folder before running the summary generation script (`5_get_vs_summary_v1.py`). This script must be run once for every binding site folder after docking calculations.
* Create `Summary_tables` folder before running the structured summary generation script (`6_tabulate_summary_files_v1.py`).  This script must be run once for every binding site folder after raw summary generation.
* Existing HCV RNA-targeted inhibitors are provided in the `data` folder, but DrugBank dataset is not provided since its license does not permit free distribution. Please download DrugBank dataset using your academic credentials before similarity analysis.
* Create `fingeRNAt_input` folder before running the input file preparation script (`8_prepare_fingernat_input_sdf_v1.py`).
* fingeRNAt package files must be present in the same directory as the `9_run_fingernat_v1.py` script. The output files will be written to the `output/fingeRNAt_input/` folder itself and must be moved to another directory (`output/fingeRNAt_output/`).
* Create `Interaction_analysis` folder before running the interaction summary generation script (`10_analyze_fingernat_output_v1.py`).

# License: MIT License










