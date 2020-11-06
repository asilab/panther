#!/bin/bash
#
# Create HDC function features
bash HDC_print_features.sh

# Create numpy features with labels
python3.6 ../python/complexity_extraction_dataset.py
python3.6 ../python/prepare_data.py