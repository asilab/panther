#!/bin/bash
ls Paintings91/Images/ | tr '.' '\t' | awk '{print $1}' | tr -d -c '[A-Z][a-z][-_\n]'  | sort -V | uniq | sed 's/.$//' > authors.txt
