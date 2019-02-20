<p align="center">
<img src="imgs/logo.png" alt="Panther" width="200" border="0" /></p>
<br>
<p align="center">
Measuring statistical information of artistic paintings
</p>

## INSTALL
Get PANThER project using:
```bash
git clone https://github.com/pratas/panther.git
cd panther/
```

## RUN
Move to the src/ directory and give run permissions
```
cd src/
chmod +x *.sh
```
an use the following instructions.

First, install and download the dataset:
```
./Install.sh
./Dataset.sh
```

To benchmark the compressors, use the following command:
```
./Benchmark.sh
```

To assess the normality properties, use the following command:
```
./Idempotency.sh
./Symmetry.sh
./Triangular.sh
```

To assess the impact of uniform substitutions of pixels, use the following command:
``` 
./Editions.sh
```

To run results, use the following command in the src dir:
```bash
./Run.sh
``` 
This will run automatically the following scripts:
```bash
./Install.sh
./Dataset.sh
./Quantize.sh
./Compress.sh
./Average.sh
./NCC.sh
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

