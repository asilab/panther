<p align="center">
<img src="imgs/logo.png" alt="Panther" width="200" border="0" /></p>
<br>
<p align="center">
Measuring probabilistic-algorithmic information of artistic paintings
</p>

## INSTALL
Get PANThER project using:
```bash
git clone https://github.com/asilab/panther.git
cd panther/

```

## RUN
Give run permissions
```
chmod +x *.sh
bash make.sh
pip3 install -r requirements.txt 
```
an use the following instructions.

To run the pipeline and obtain all the Reports in the folder reports, use the following command in the src dir:
```bash
./Run.sh
``` 

This will run automatically the following scripts:
```bash

./Dataset.sh                        # Downloads and unzips dataset
./Quantize.sh                       # Quantizes images of the dataset to 8, 6, 4 and 2 bits.
./Trimm_and_Binarization.sh         # Trims and Binarizes images of the dataset.
./BDM.sh                            # Computes NBDM (1 and 2) for all quantized images of the dataset.
./Compress.sh                       # Computes NC for all quantized images of the dataset.
./HDC.sh                            # Computes HDC alpha for 8 bit quantized images of the dataset.
./Average_Complexity.sh             # Computes average information based measures for each author
./Region_Complexity.sh              # Computes regional NC for 8 bit quantized images of the dataset.
./Average_Regional_Complexity.sh    # Computes fingerprint of each author

```

To download and prepare the dataset, use the following command:
```
./Dataset.sh
```

To benchmark the compressors, use the following command:
```
./Benchmark.sh
```

To quantitize images run, to trim and binarize, use the following command:
```
./Quantize.sh                     
./Trimm_and_Binarization.sh 
```

To perform comparisson between NC, NBDM1 and NBDM2, use the following command:
``` 
./Compare.sh
```

To compute the average NC, NBDM1, and NBDM2 for each author, use the following command:
``` 
./Average_Complexity.sh
```

To compute the NC with the HDC results, use the following command: 
``` 
./NC_HDC.sh
```

To recreate the authors' fingerprints, use the following command: 
``` 
./Fingerprints.sh
```

To recreate the phylogenic tree, use the following command: 
``` 
./Tree.sh
```

To assess the normality proerties, use the following command:
```
./Idempotency.sh
./Symmetry.sh
./Triangular.sh
```

## CITE
Please cite the followings, if you use PANThER:
* Processing...

## RELEASES
* [Release](https://github.com/pratas/panther/releases) 1.

## ISSUES
Please let us know if there is any
[issues](https://github.com/pratas/panther/issues).


## LICENSE
PANThER is under GPL v3 license. For more information, click
[here](http://www.gnu.org/licenses/gpl-3.0.html).

