set grid ytics
set grid xtics
set nokey
set ytics 1
set xtics 1

set term png size 1500,500

set title "ESCALONADOR DE PROCESSOS - FIRST COME FIRST SERVED"

set ylabel "Processos a serem executados"
set xlabel "Ciclos de clock"

plot 'fcfs.dat' with points pointtype 5 pointsize 4 lc rgb "red" title "Processos em Execucao"
replot 'fcfs.dat' using 1:2:(sprintf("(%d)", $3)) with labels

set terminal png
set output 'fcfs.png'
replot
