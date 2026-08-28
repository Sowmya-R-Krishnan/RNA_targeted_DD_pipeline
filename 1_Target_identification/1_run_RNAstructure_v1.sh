#!/bin/bash

#Shell script to run RNAstructure for folding an RNA sequence with SHAPE restraints
Fold data/H77_sequence.fasta output/H77_folding_trial_w4000.ct -sh data/H77_SHAPE_restraints.csv -sm 1.8 -si -0.6 -w 4000 -md 500 -mfe
