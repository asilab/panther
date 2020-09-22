#!/bin/bash
#
##Create Fingerprints as HeatMaps
rm -R ../local_region_complexity_256/*
mkdir ../local_region_complexity_256
Report_path="../reports/REPORT_AVG_REGIONAL_COMPLEXITY_PER_BLOCK_256"
python ../python/heatmap.py $Report_path