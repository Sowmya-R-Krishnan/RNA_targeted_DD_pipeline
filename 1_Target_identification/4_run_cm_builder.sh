#!/bin/bash

#Shell script to automate covariance model calibration
declare -a stable_regions=("1010_1050" "1277_1293" "1320_1534" "2049_2117" "2287_2362" "2520_2561" "3293_3362" "3716_3799" "3864_3895" "4558_4671" "4873_4968" "49_114" "5297_5411" "5444_5499" "5807_5876" "592_663" "5999_6074" "6518_6635" "6918_6929" "762_816" "8136_8145" "8419_8471" "8681_8702" "9223_9311" "9397_9512")

for index in ${!stable_regions[*]}
do 
	region=${stable_regions[$index]}
	
	#Run cm-builder
	./cm-builder -m output/Stable_regions/H77_region_${region}.db -d data/HCV_genotype_1.fasta -O -s data/H77_sequence.fasta -g -r -S -k -c 4 -M output/Infernal_results/H77_${region}/ -o output/Infernal_results/H77_${region}/ -E 10 -D 2
	
	#Polish stockholm alignments
	./stockholmPolish -o output/Infernal_results/H77_${region}/Stockholm_polish1/ -kad output/Infernal_results/H77_${region}/H77_1.stockholm
	./stockholmPolish -o output/Infernal_results/H77_${region}/Stockholm_polish2/ -kad output/Infernal_results/H77_${region}/H77_2.stockholm
	./stockholmPolish -o output/Infernal_results/H77_${region}/Stockholm_polish3/ -kad output/Infernal_results/H77_${region}/H77_3.stockholm
	mv output/Infernal_results/H77_${region}/Stockholm_polish1/H77_1.stockholm output/Infernal_results/H77_${region}/H77_1_polished.stockholm
	rm -r output/Infernal_results/H77_${region}/Stockholm_polish1/
	mv output/Infernal_results/H77_${region}/Stockholm_polish2/H77_2.stockholm output/Infernal_results/H77_${region}/H77_2_polished.stockholm
	rm -r output/Infernal_results/H77_${region}/Stockholm_polish2/
	mv output/Infernal_results/H77_${region}/Stockholm_polish3/H77_3.stockholm output/Infernal_results/H77_${region}/H77_3_polished.stockholm
	rm -r output/Infernal_results/H77_${region}/Stockholm_polish3/
	
	#Run R-scape
	mkdir output/Infernal_results/H77_${region}/R-scape_results
	rscape/bin/R-scape -s -E 0.1 --outdir output/Infernal_results/H77_${region}/R-scape_results/ --lancaster output/Infernal_results/H77_${region}/H77_3_polished.stockholm
	rscape/bin/r2r --GSC-weighted-consensus output/Infernal_results/H77_${region}/R-scape_results/H77_3_polished.stockholm_1.R2R.sto output/Infernal_results/H77_${region}/H77_3_polished_R2R.sto 3 0.97 0.9 0.75 4 0.97 0.9 0.75 0.5 0.1
	rscape/bin/r2r --disable-usage-warning output/Infernal_results/H77_${region}/H77_3_polished_R2R.sto output/Infernal_results/H77_${region}/H77_3_polished_R2R.pdf
	rscape/bin/r2r --disable-usage-warning output/Infernal_results/H77_${region}/H77_3_polished_R2R.sto output/Infernal_results/H77_${region}/H77_3_polished_R2R.svg
	
	printf "${region}\n"
done




















