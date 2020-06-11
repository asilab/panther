#!/bin/bash
#

RUN_HDC=0;
RUN_NC=1;
NC_PLOT=1;
DELTA_NC=0;
RUN_NBDM=1;
NBMD_PLOT=1;
DELTA_BDM=0;
DELTA=0;
#
# ==============================================================================
#
if [[ "$RUN_NC" -eq "1" ]]; then
  declare -a NAMES=( "ALBRECHT_DURER" "AMEDEO_MODIGLIANI" "ANDREA_MANTEGNA" "ANDY_WARHOL" "ARSHILLE_GORKY" "CAMILLE_COROT" "CARAVAGGIO" "CASPAR_DAVID_FRIEDRICH" "CLAUDE_LORRAIN" "CLAUDE_MONET" "DANTE_GABRIEL_ROSSETTI" "DAVID_HOCKNEY" "DIEGO_VELAZQUEZ" "EDGAR_DEGAS" "EDVARD_MUNCH" "EDWARD_HOPPER" "EGON_SCHIELE" "EL_LISSITZKY" "EUGENE_DELACROIX" "FERNAND_LEGER" "FRANCISCO_DE_GOYA" "FRANCISCO_DE_ZURBARAN" "FRANCIS_BACON" "FRANS_HALS" "FRANZ_MARC" "FRA_ANGELICO" "FRIDA_KAHLO" "Frederic_Edwin_Church" "GENTILESCHI_ARTEMISIA" "GEORGES_BRAQUE" "GEORGES_DE_LA_TOUR" "GEORGES_SEURAT" "GEORGIA_OKEEFE" "GERHARD_RICHTER" "GIORGIONE" "GIORGIO_DE_CHIRICO" "GIOTTO_DI_BONDONE" "GUSTAVE_COURBET" "GUSTAVE_MOREAU" "GUSTAV_KLIMT" "HANS_HOLBEIN_THE_YOUNGER" "HANS_MEMLING" "HENRI_MATISSE" "HIERONYMUS_BOSCH" "JACKSON_POLLOCK" "JACQUES-LOUIS_DAVID" "JAMES_ENSOR" "JAMES_MCNEILL_WHISTLER" "JAN_VAN_EYCK" "JAN_VERMEER" "JASPER_JOHNS" "JEAN-ANTOINE_WATTEAU" "JEAN-AUGUSTE-DOMINIQUE_INGRES" "JEAN-MICHEL_BASQUIAT" "JEAN_FRANCOIS_MILLET" "JOACHIM_PATINIR" "JOAN_MIRO" "JOHN_CONSTABLE" "JOSEPH_MALLORD_WILLIAM_TURNER" "KAZIMIR_MALEVICH" "LUCIO_FONTANA" "MARC_CHAGALL" "MARK_ROTHKO" "MAX_ERNST" "NICOLAS_POUSSIN" "PAUL_CEZANNE" "PAUL_GAUGUIN" "PAUL_KLEE" "PETER_PAUL_RUBENS" "PIERRE-AUGUSTE_RENOIR" "PIETER_BRUEGEL_THE_ELDER" "PIET_MONDRIAN" "Picasso" "RAPHAEL" "REMBRANDT_VAN_RIJN" "RENE_MAGRITTE" "ROGER_VAN_DER_WEYDEN" "ROY_LICHTENSTEIN" "SALVADOR_DALI" "SANDRO_BOTTICELLI" "THEODORE_GERICAULT" "TINTORETTO" "TITIAN" "UMBERTO_BOCCIONI" "VINCENT_VAN_GOGH" "WASSILY_KANDINSKY" "WILLEM_DE_KOONING" "WILLIAM_BLAKE" "WILLIAM_HOGARTH" "WINSLOW_HOMER" "DOUARD_MANET" )
  declare -a QUANTITIZATION=("Quantizing2" "Quantizing4" "Quantizing6" "Quantizing8");
  number_painters=$(echo "${#NAMES[@]}");
  for a in `seq 1 $number_painters `;
    do
      echo "scale=0; ($a * 16777216) / $number_painters " | bc -l >> TMP_color
  done 
  
  for j in "${QUANTITIZATION[@]}"
    do
    rm -f NC_AVERAGE_TMP;
    rm -f ../reports/NC_AVERAGE_$j;
    for i in "${NAMES[@]}"
    do
      SUM=`cat ../reports/REPORT_COMPLEXITY_NC_$j | grep -a $i | awk 'BEGIN {t=0}; {t+=$3} END {print t}'`;
      CAR=`cat ../reports/REPORT_COMPLEXITY_NC_$j | grep -a $i | wc -l`;
      printf "\"$i\"" >> NC_AVERAGE_TMP;
      echo "scale=8; ($SUM / $CAR)" | bc -l | awk '{printf "\t%f\t", $0}' >> NC_AVERAGE_TMP;
      printf "$CAR\n" >> NC_AVERAGE_TMP;
    done
    #
    sort -k 1 NC_AVERAGE_TMP > NC_TMP;
    paste NC_TMP TMP_color > NC_AVERAGE_TMP;
    sort -k 2 -V NC_AVERAGE_TMP >  TEMP_AVERAGE_NC;
    number_of_lines=$(wc -l TEMP_AVERAGE_NC | awk '{print $1}');
    seq 1 $number_of_lines > TEMP_SEQ;
    paste TEMP_AVERAGE_NC TEMP_SEQ > ../reports/NC_AVERAGE_$j;
  done
  #
  rm TMP_color NC_AVERAGE_TMP NC_TMP TEMP_AVERAGE_NC TEMP_SEQ;
fi
# ==============================================================================
#

if [[ "$RUN_HDC" -eq "1" ]]; then
  
  declare -a NAMES=( "ALBRECHT_DURER" "AMEDEO_MODIGLIANI" "ANDREA_MANTEGNA" "ANDY_WARHOL" "ARSHILLE_GORKY" "CAMILLE_COROT" "CARAVAGGIO" "CASPAR_DAVID_FRIEDRICH" "CLAUDE_LORRAIN" "CLAUDE_MONET" "DANTE_GABRIEL_ROSSETTI" "DAVID_HOCKNEY" "DIEGO_VELAZQUEZ" "EDGAR_DEGAS" "EDVARD_MUNCH" "EDWARD_HOPPER" "EGON_SCHIELE" "EL_LISSITZKY" "EUGENE_DELACROIX" "FERNAND_LEGER" "FRANCISCO_DE_GOYA" "FRANCISCO_DE_ZURBARAN" "FRANCIS_BACON" "FRANS_HALS" "FRANZ_MARC" "FRA_ANGELICO" "FRIDA_KAHLO" "Frederic_Edwin_Church" "GENTILESCHI_ARTEMISIA" "GEORGES_BRAQUE" "GEORGES_DE_LA_TOUR" "GEORGES_SEURAT" "GEORGIA_OKEEFE" "GERHARD_RICHTER" "GIORGIONE" "GIORGIO_DE_CHIRICO" "GIOTTO_DI_BONDONE" "GUSTAVE_COURBET" "GUSTAVE_MOREAU" "GUSTAV_KLIMT" "HANS_HOLBEIN_THE_YOUNGER" "HANS_MEMLING" "HENRI_MATISSE" "HIERONYMUS_BOSCH" "JACKSON_POLLOCK" "JACQUES-LOUIS_DAVID" "JAMES_ENSOR" "JAMES_MCNEILL_WHISTLER" "JAN_VAN_EYCK" "JAN_VERMEER" "JASPER_JOHNS" "JEAN-ANTOINE_WATTEAU" "JEAN-AUGUSTE-DOMINIQUE_INGRES" "JEAN-MICHEL_BASQUIAT" "JEAN_FRANCOIS_MILLET" "JOACHIM_PATINIR" "JOAN_MIRO" "JOHN_CONSTABLE" "JOSEPH_MALLORD_WILLIAM_TURNER" "KAZIMIR_MALEVICH" "LUCIO_FONTANA" "MARC_CHAGALL" "MARK_ROTHKO" "MAX_ERNST" "NICOLAS_POUSSIN" "PAUL_CEZANNE" "PAUL_GAUGUIN" "PAUL_KLEE" "PETER_PAUL_RUBENS" "PIERRE-AUGUSTE_RENOIR" "PIETER_BRUEGEL_THE_ELDER" "PIET_MONDRIAN" "Picasso" "RAPHAEL" "REMBRANDT_VAN_RIJN" "RENE_MAGRITTE" "ROGER_VAN_DER_WEYDEN" "ROY_LICHTENSTEIN" "SALVADOR_DALI" "SANDRO_BOTTICELLI" "THEODORE_GERICAULT" "TINTORETTO" "TITIAN" "UMBERTO_BOCCIONI" "VINCENT_VAN_GOGH" "WASSILY_KANDINSKY" "WILLEM_DE_KOONING" "WILLIAM_BLAKE" "WILLIAM_HOGARTH" "WINSLOW_HOMER" "DOUARD_MANET" )
  declare -a QUANTITIZATION=("Quantizing2" "Quantizing4" "Quantizing6" "Quantizing8");
  number_painters=$(echo "${#NAMES[@]}");
  for a in `seq 1 $number_painters `;
    do
      echo "scale=0; ($a * 16777216) / $number_painters " | bc -l >> TMP_color
  done 
  
  for j in "${QUANTITIZATION[@]}"
    do
    rm -f HDC_AVERAGE_TMP;
    rm -f ../reports/HDC_AVERAGE_$j;
    for i in "${NAMES[@]}"
    do
      SUM=`cat ../reports/REPORT_COMPLEXITY_HDC_$j | grep -a $i | awk 'BEGIN {t=0}; {t+=$3} END {print t}'`;
      CAR=`cat ../reports/REPORT_COMPLEXITY_HDC_$j | grep -a $i | wc -l`;
      printf "\"$i\"" >> HDC_AVERAGE_TMP;
      echo "scale=8; ($SUM / $CAR)" | bc -l | awk '{printf "\t%f\t", $0}' >> HDC_AVERAGE_TMP;
      printf "$CAR\n" >> HDC_AVERAGE_TMP;
    done
    #
    sort -k 1 HDC_AVERAGE_TMP > HDC_TMP;
    paste HDC_TMP TMP_color > HDC_AVERAGE_TMP;
    sort -k 2 -V HDC_AVERAGE_TMP >  TEMP_AVERAGE_HDC;
    number_of_lines=$(wc -l TEMP_AVERAGE_HDC | awk '{print $1}');
    seq 1 $number_of_lines > TEMP_SEQ;
    paste TEMP_AVERAGE_HDC TEMP_SEQ > ../reports/HDC_AVERAGE_$j;
  done
  #
  rm TMP_color HDC_AVERAGE_TMP HDC_TMP TEMP_AVERAGE_HDC TEMP_SEQ;

fi

# ==============================================================================
#

if [[ "$DELTA_NC" -eq "1" ]]; then
  
  awk '{print $1,"\t",$4,"\t",$5}' ../reports/NC_AVERAGE_Quantizing8 > Q8;
  sort -k 1 -o Q8 Q8;
  awk '{print $1,"\t",$4,"\t",$5}' ../reports/NC_AVERAGE_Quantizing6 > Q6;
  sort -k 1 -o Q6 Q6;
  awk '{print $1,"\t",$4,"\t",$5}' ../reports/NC_AVERAGE_Quantizing4 > Q4;
  sort -k 1 -o Q4 Q4;

  awk '{print $1,"\t",$2}' Q4 > PAINTERS_NC;
  paste <(awk '{print $3}' Q4 ) <(awk '{print $3}' Q6 ) <(awk '{print $3}' Q8) > PAINTERS_NC_POS;
  awk ' NR >= 0 { $4 = sqrt(($3 - $1)^2) } 1' PAINTERS_NC_POS > testfile.tmp && mv testfile.tmp PAINTERS_NC_POS;
  awk ' NR >= 0 { $5 = sqrt(($3 - $2)^2) } 1' PAINTERS_NC_POS > testfile.tmp && mv testfile.tmp PAINTERS_NC_POS;
  paste PAINTERS_NC <(awk '{print $4,"\t",$5}' PAINTERS_NC_POS) > testfile.tmp && mv testfile.tmp PAINTERS_NC_POS;
  sort -n -k 3 -o PAINTERS_NC_POS PAINTERS_NC_POS;
  rm Q4 Q6 Q8 PAINTERS_NC;
  echo "Plotting circular NC...";
  python3 circular_chart.py PAINTERS_NC_POS

fi

# ==============================================================================
if [[ "$NC_PLOT" -eq "1" ]]; then
  echo "Plotting NC";

  gnuplot << EOF
  reset
  set terminal pdfcairo enhance color
  set term pdfcairo font 'Tahoma,7'
  set key under nobox
  set style histogram clustered gap 1 title offset 1,0.25
  unset xtics
  set output 'Artists_NC.pdf'
  set auto
  set boxwidth 0.5 relative 
  set style fill solid 0.75 noborder
  set ylabel 'NC' font 'Tahoma,8'
  set xlabel 'Authors' font 'Tahoma,8'
  set grid ytics lc rgb '#C0C0C0'
  set key ins horiz font 'Tahoma,8'
  set key center top
  set xtics rotate nomirror
  set tics textcolor rgb 'black'
  set yrange[0:1]
  set grid
  set xtics 0.2 nomirror font 'Tahoma,5' noenhance "_"
  set ytics 0.2 nomirror font 'Tahoma,8'
  plot '../reports/NC_AVERAGE_Quantizing8' using 0:2:4:xticlabels(1) with boxes lc rgb variable title 'Average NC, 8 bits Quantitization'
  plot '../reports/NC_AVERAGE_Quantizing6' using 0:2:4:xticlabels(1) with boxes lc rgb variable title 'Average NC, 6 bits Quantitization' 
  set yrange[0:0.6]
  plot '../reports/NC_AVERAGE_Quantizing4' using 0:2:4:xticlabels(1) with boxes lc rgb variable title 'Average NC, 4 bits Quantitization' 
  plot '../reports/NC_AVERAGE_Quantizing2' using 0:2:4:xticlabels(1) with boxes lc rgb variable title 'Average NC, 2 bits Quantitization' 
EOF

mv Artists_NC.pdf ../plots/;
fi
#
#
# ==============================================================================
#
if [[ "$RUN_NBDM" -eq "1" ]]; then
  declare -a NAMES=( "ALBRECHT_DURER" "AMEDEO_MODIGLIANI" "ANDREA_MANTEGNA" "ANDY_WARHOL" "ARSHILLE_GORKY" "CAMILLE_COROT" "CARAVAGGIO" "CASPAR_DAVID_FRIEDRICH" "CLAUDE_LORRAIN" "CLAUDE_MONET" "DANTE_GABRIEL_ROSSETTI" "DAVID_HOCKNEY" "DIEGO_VELAZQUEZ" "EDGAR_DEGAS" "EDVARD_MUNCH" "EDWARD_HOPPER" "EGON_SCHIELE" "EL_LISSITZKY" "EUGENE_DELACROIX" "FERNAND_LEGER" "FRANCISCO_DE_GOYA" "FRANCISCO_DE_ZURBARAN" "FRANCIS_BACON" "FRANS_HALS" "FRANZ_MARC" "FRA_ANGELICO" "FRIDA_KAHLO" "Frederic_Edwin_Church" "GENTILESCHI_ARTEMISIA" "GEORGES_BRAQUE" "GEORGES_DE_LA_TOUR" "GEORGES_SEURAT" "GEORGIA_OKEEFE" "GERHARD_RICHTER" "GIORGIONE" "GIORGIO_DE_CHIRICO" "GIOTTO_DI_BONDONE" "GUSTAVE_COURBET" "GUSTAVE_MOREAU" "GUSTAV_KLIMT" "HANS_HOLBEIN_THE_YOUNGER" "HANS_MEMLING" "HENRI_MATISSE" "HIERONYMUS_BOSCH" "JACKSON_POLLOCK" "JACQUES-LOUIS_DAVID" "JAMES_ENSOR" "JAMES_MCNEILL_WHISTLER" "JAN_VAN_EYCK" "JAN_VERMEER" "JASPER_JOHNS" "JEAN-ANTOINE_WATTEAU" "JEAN-AUGUSTE-DOMINIQUE_INGRES" "JEAN-MICHEL_BASQUIAT" "JEAN_FRANCOIS_MILLET" "JOACHIM_PATINIR" "JOAN_MIRO" "JOHN_CONSTABLE" "JOSEPH_MALLORD_WILLIAM_TURNER" "KAZIMIR_MALEVICH" "LUCIO_FONTANA" "MARC_CHAGALL" "MARK_ROTHKO" "MAX_ERNST" "NICOLAS_POUSSIN" "PAUL_CEZANNE" "PAUL_GAUGUIN" "PAUL_KLEE" "PETER_PAUL_RUBENS" "PIERRE-AUGUSTE_RENOIR" "PIETER_BRUEGEL_THE_ELDER" "PIET_MONDRIAN" "Picasso" "RAPHAEL" "REMBRANDT_VAN_RIJN" "RENE_MAGRITTE" "ROGER_VAN_DER_WEYDEN" "ROY_LICHTENSTEIN" "SALVADOR_DALI" "SANDRO_BOTTICELLI" "THEODORE_GERICAULT" "TINTORETTO" "TITIAN" "UMBERTO_BOCCIONI" "VINCENT_VAN_GOGH" "WASSILY_KANDINSKY" "WILLEM_DE_KOONING" "WILLIAM_BLAKE" "WILLIAM_HOGARTH" "WINSLOW_HOMER" "DOUARD_MANET" )
  declare -a QUANTITIZATION=("Quantizing2" "Quantizing4" "Quantizing6" "Quantizing8");
  number_painters=$(echo "${#NAMES[@]}");
  for a in `seq 1 $number_painters `;
    do
      echo "scale=0; ($a * 16777216) / $number_painters " | bc -l >> TMP_color
  done 
  
  for j in "${QUANTITIZATION[@]}"
    do
    rm -f PYBDM_AVERAGE_TMP;
    rm -f ../reports/NBDM_AVERAGE1_$j;
    for i in "${NAMES[@]}"
    do
      SUM=`cat ../reports/REPORT_COMPLEXITY_NBDM1_$j | grep -a $i | awk 'BEGIN {t=0}; {t+=$3} END {print t}'`;
      CAR=`cat  ../reports/REPORT_COMPLEXITY_NBDM1_$j | grep -a $i | wc -l`;
      printf "\"$i\"" >> PYBDM_AVERAGE_TMP;
      echo "scale=8; ($SUM / $CAR)" | bc -l | awk '{printf "\t%f\t", $0}' >> PYBDM_AVERAGE_TMP;
      printf "$CAR\n" >> PYBDM_AVERAGE_TMP;
    done

    sort -k 1 PYBDM_AVERAGE_TMP > BDM_TMP;
    paste BDM_TMP TMP_color > PYBDM_AVERAGE_TMP;
    sort -k 2 -V PYBDM_AVERAGE_TMP >  TEMP_AVERAGE_BDM;
    number_of_lines=$(wc -l TEMP_AVERAGE_BDM | awk '{print $1}');
    seq 1 $number_of_lines > TEMP_SEQ;
    paste TEMP_AVERAGE_BDM TEMP_SEQ > ../reports/NBDM_AVERAGE1_$j;
  done
  #
  rm PYBDM_AVERAGE_TMP BDM_TMP TEMP_AVERAGE_BDM TEMP_SEQ;

 for j in "${QUANTITIZATION[@]}"
    do
    rm -f PYBDM_AVERAGE_TMP;
    rm -f ../reports/NBDM_AVERAGE2_$j;
    for i in "${NAMES[@]}"
    do
      SUM=`cat ../reports/REPORT_COMPLEXITY_NBDM2_$j | grep -a $i | awk 'BEGIN {t=0}; {t+=$3} END {print t}'`;
      CAR=`cat  ../reports/REPORT_COMPLEXITY_NBDM2_$j | grep -a $i | wc -l`;
      printf "\"$i\"" >> PYBDM_AVERAGE_TMP;
      echo "scale=8; ($SUM / $CAR)" | bc -l | awk '{printf "\t%f\t", $0}' >> PYBDM_AVERAGE_TMP;
      printf "$CAR\n" >> PYBDM_AVERAGE_TMP;
    done

    sort -k 1 PYBDM_AVERAGE_TMP > BDM_TMP;
    paste BDM_TMP TMP_color > PYBDM_AVERAGE_TMP;
    sort -k 2 -V PYBDM_AVERAGE_TMP >  TEMP_AVERAGE_BDM;
    number_of_lines=$(wc -l TEMP_AVERAGE_BDM | awk '{print $1}');
    seq 1 $number_of_lines > TEMP_SEQ;
    paste TEMP_AVERAGE_BDM TEMP_SEQ > ../reports/NBDM_AVERAGE2_$j;
  done
  #
  rm TMP_color PYBDM_AVERAGE_TMP BDM_TMP TEMP_AVERAGE_BDM TEMP_SEQ;

fi
# ==============================================================================
#
if [[ "$NBMD_PLOT" -eq "1" ]]; then
echo "Plotting BDM Normalized by number of bits";
gnuplot << EOF
  reset
  set terminal pdfcairo enhance color
  set term pdfcairo font 'Tahoma,7'
  set key under nobox
  set style histogram clustered gap 1 title offset 1,0.25
  unset xtics
  set output 'Artists_NBDM1.pdf'
  set auto
  set boxwidth 0.5 relative 
  set style fill solid 0.75 noborder
  set ylabel 'NBDM1' font 'Tahoma,8'
  set xlabel 'Authors' font 'Tahoma,8'
  set grid ytics lc rgb '#C0C0C0'
  set key ins horiz font 'Tahoma,8'
  set key center top
  set xtics rotate nomirror
  set tics textcolor rgb 'black'
  set yrange[0:1]
  set grid
  set xtics 0.2 nomirror font 'Tahoma,5' noenhance "_"
  set ytics 0.2 nomirror font 'Tahoma,8'
  plot '../reports/NBDM_AVERAGE1_Quantizing8' using 0:2:4:xticlabels(1) with boxes lc rgb variable title 'Average NBDM, 8 bits Quantitization'
  plot '../reports/NBDM_AVERAGE1_Quantizing6' using 0:2:4:xticlabels(1) with boxes lc rgb variable title 'Average NBDM, 6 bits Quantitization' 
  plot '../reports/NBDM_AVERAGE1_Quantizing4' using 0:2:4:xticlabels(1) with boxes lc rgb variable title 'Average NBDM, 4 bits Quantitization' 
  set yrange[0:0.05]
  plot '../reports/NBDM_AVERAGE1_Quantizing2' using 0:2:4:xticlabels(1) with boxes lc rgb variable title 'Average NBDM, 2 bits Quantitization' 
EOF
mv Artists_NBDM1.pdf ../plots/;


echo "Plotting BDM Dynamic Normalization";
gnuplot << EOF
  reset
  set terminal pdfcairo enhance color
  set term pdfcairo font 'Tahoma,7'
  set key under nobox
  set style histogram clustered gap 1 title offset 1,0.25
  unset xtics
  set output 'Artists_NBDM2.pdf'
  set auto
  set boxwidth 0.5 relative 
  set style fill solid 0.75 noborder
  set ylabel 'NBDM2' font 'Tahoma,8'
  set xlabel 'Authors' font 'Tahoma,8'
  set grid ytics lc rgb '#C0C0C0'
  set key ins horiz font 'Tahoma,8'
  set key center top
  set xtics rotate nomirror
  set tics textcolor rgb 'black'
  set yrange[0:0.6]
  set grid
  set xtics 0.2 nomirror font 'Tahoma,5' noenhance "_"
  set ytics 0.2 nomirror font 'Tahoma,8'
  plot '../reports/NBDM_AVERAGE2_Quantizing8' using 0:2:4:xticlabels(1) with boxes lc rgb variable title 'Average NBDM, 8 bits Quantitization'
  plot '../reports/NBDM_AVERAGE2_Quantizing6' using 0:2:4:xticlabels(1) with boxes lc rgb variable title 'Average NBDM, 6 bits Quantitization' 
  plot '../reports/NBDM_AVERAGE2_Quantizing4' using 0:2:4:xticlabels(1) with boxes lc rgb variable title 'Average NBDM, 4 bits Quantitization' 
  set yrange[0:0.05]
  plot '../reports/NBDM_AVERAGE2_Quantizing2' using 0:2:4:xticlabels(1) with boxes lc rgb variable title 'Average NBDM, 2 bits Quantitization' 
EOF
mv Artists_NBDM2.pdf ../plots/;

fi
# 

if [[ "$DELTA_BDM" -eq "1" ]]; then
  
  awk '{print $1,"\t",$4,"\t",$5}' ../reports/NBDM_AVERAGE1_Quantizing8 > Q8;
  sort -k 1 -o Q8 Q8;
  awk '{print $1,"\t",$4,"\t",$5}' ../reports/NBDM_AVERAGE1_Quantizing6 > Q6;
  sort -k 1 -o Q6 Q6;
  awk '{print $1,"\t",$4,"\t",$5}' ../reports/NBDM_AVERAGE1_Quantizing4 > Q4;
  sort -k 1 -o Q4 Q4;

  awk '{print $1,"\t",$2}' Q4 > PAINTERS_BDM;
  paste <(awk '{print $3}' Q4 ) <(awk '{print $3}' Q6 ) <(awk '{print $3}' Q8) > PAINTERS_BDM_1_POS;
  awk ' NR >= 0 { $4 = sqrt(($3 - $1)^2) } 1' PAINTERS_BDM_1_POS > testfile.tmp && mv testfile.tmp PAINTERS_BDM_1_POS;
  awk ' NR >= 0 { $5 = sqrt(($3 - $2)^2) } 1' PAINTERS_BDM_1_POS > testfile.tmp && mv testfile.tmp PAINTERS_BDM_1_POS;
  paste PAINTERS_BDM <(awk '{print $4,"\t",$5}' PAINTERS_BDM_1_POS) > testfile.tmp && mv testfile.tmp PAINTERS_BDM_1_POS;
  sort -n -k 3 -o PAINTERS_BDM_1_POS PAINTERS_BDM_1_POS;
    echo "Plotting circular NBDM1...";
  python3 circular_chart.py PAINTERS_BDM_1_POS

  rm Q4 Q6 Q8 PAINTERS_BDM;


  awk '{print $1,"\t",$4,"\t",$5}' ../reports/NBDM_AVERAGE2_Quantizing8 > Q8;
  sort -k 1 -o Q8 Q8;
  awk '{print $1,"\t",$4,"\t",$5}' ../reports/NBDM_AVERAGE2_Quantizing6 > Q6;
  sort -k 1 -o Q6 Q6;
  awk '{print $1,"\t",$4,"\t",$5}' ../reports/NBDM_AVERAGE2_Quantizing4 > Q4;
  sort -k 1 -o Q4 Q4;

  awk '{print $1,"\t",$2}' Q4 > PAINTERS_BDM;
  paste <(awk '{print $3}' Q4 ) <(awk '{print $3}' Q6 ) <(awk '{print $3}' Q8) > PAINTERS_BDM_2_POS;
  awk ' NR >= 0 { $4 = sqrt(($3 - $1)^2) } 1' PAINTERS_BDM_2_POS > testfile.tmp && mv testfile.tmp PAINTERS_BDM_2_POS;
  awk ' NR >= 0 { $5 = sqrt(($3 - $2)^2) } 1' PAINTERS_BDM_2_POS > testfile.tmp && mv testfile.tmp PAINTERS_BDM_2_POS;
  paste PAINTERS_BDM <(awk '{print $4,"\t",$5}' PAINTERS_BDM_2_POS) > testfile.tmp && mv testfile.tmp PAINTERS_BDM_2_POS;
  sort -n -k 3 -o PAINTERS_BDM_2_POS PAINTERS_BDM_2_POS;
  echo "Plotting circular NBDM2...";
  python3 circular_chart.py PAINTERS_BDM_2_POS

  rm Q4 Q6 Q8 PAINTERS_BDM;

fi

if [[ "$DELTA" -eq "1" ]]; then
sort -k 1 -o PAINTERS_NC_POS PAINTERS_NC_POS
sort -k 1 -o PAINTERS_BDM_1_POS PAINTERS_BDM_1_POS
paste <(awk '{print $1,"\t",$2,"\t",$3}' PAINTERS_NC_POS) <(awk '{print $3}' PAINTERS_BDM_1_POS) > PAINTERS_1_DELTA
rm PAINTERS_BDM_1_POS;

sort -k 1 -o PAINTERS_BDM_2_POS PAINTERS_BDM_2_POS
paste <(awk '{print $1,"\t",$2,"\t",$3}' PAINTERS_NC_POS) <(awk '{print $3}' PAINTERS_BDM_2_POS) > PAINTERS_2_DELTA
rm PAINTERS_BDM_2_POS PAINTERS_NC_POS;
echo "Plotting delta NBDM1 and NBDM2...";

gnuplot << EOF 
  reset
  set terminal pdfcairo enhance color
  set term pdfcairo font 'Tahoma,7'
  set key under nobox
  set style histogram clustered gap 1 title offset 1,0.25
  set style fill solid noborder
  unset xtics
  set output 'delta.pdf'
  set auto
  set boxwidth 1
  set style fill solid 1.00
  set grid ytics lc rgb '#C0C0C0'
  set key ins horiz font 'Tahoma,8'
  set key center top
  set style fill solid 1.0 border 0.5
  set xtics rotate nomirror
  set tics textcolor rgb 'black'
  set yrange[0.75:55]
  set xrange[0.75:55]
  set size square
  set ylabel 'NBDM1' font 'Tahoma,8'
  set xlabel 'NC' font 'Tahoma,8'
  set key outside
  set pointsize 0.6
  set logscale x 2
  set logscale y 2

  set style line 1 lw 1.5 lc rgb variable pt 6   
  set title 'Painters delta'  font 'Tahoma,8'
  set datafile separator "\t"
  plot 'PAINTERS_1_DELTA' using 3:4:2 notitle with points ls 1 ,\
  'PAINTERS_1_DELTA' using 3:4:1 notitle with labels font 'Tahoma,1.5'  offset char 0.1,-0.6 noenhance "_"
  set ylabel 'NBDM2' font 'Tahoma,8'
  plot 'PAINTERS_2_DELTA' using 3:4:2 notitle with points ls 1 ,\
  'PAINTERS_2_DELTA' using 3:4:1 notitle with labels font 'Tahoma,1.5'  offset char 0.1,-0.6 noenhance "_"
EOF

SUM_NC=`cat PAINTERS_1_DELTA | awk 'BEGIN {t=0}; {t+=$3} END {print t}'`;
SUM_NBDM1=`cat PAINTERS_1_DELTA | awk 'BEGIN {t=0}; {t+=$4} END {print t}'`;
SUM_NBDM2=`cat PAINTERS_2_DELTA | awk 'BEGIN {t=0}; {t+=$4} END {print t}'`;

CAR=`cat PAINTERS_1_DELTA | wc -l`;

STD_Delta_NC=$(awk '{sum+=$3;a[NR]=$3}END{for(i in a)y+=(a[i]-(sum/NR))^2;print sqrt(y/(NR-1))}' PAINTERS_1_DELTA);
STD_Delta_NBDM1=$(awk '{sum+=$4;a[NR]=$4}END{for(i in a)y+=(a[i]-(sum/NR))^2;print sqrt(y/(NR-1))}' PAINTERS_1_DELTA);
STD_Delta_NBDM2=$(awk '{sum+=$4;a[NR]=$4}END{for(i in a)y+=(a[i]-(sum/NR))^2;print sqrt(y/(NR-1))}' PAINTERS_2_DELTA);

Average_NC=$(echo "scale=4; ($SUM_NC / $CAR)" | bc -l | awk '{printf "\t%f\t", $0}');
Average_NBDM1=$(echo "scale=4; ($SUM_NBDM1 / $CAR)" | bc -l | awk '{printf "\t%f\t", $0}');
Average_NBDM2=$(echo "scale=4; ($SUM_NBDM2 / $CAR)" | bc -l | awk '{printf "\t%f\t", $0}');

echo "NC DELTA AVG = " $Average_NC " +/- " $STD_Delta_NC;
echo "NBDM1 DELTA AVG = "$Average_NBDM1  " +/- "  $STD_Delta_NBDM1;
echo "NBDM2 DELTA AVG = "$Average_NBDM2  " +/- " $Average_NBDM2 ;

mv delta.pdf ../plots/

rm PAINTERS_1_DELTA PAINTERS_2_DELTA;

fi
