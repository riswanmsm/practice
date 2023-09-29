#!/bin/bash

file="./arrays_table.csv"

column_0=($(cut -d "," -f 1 $file))
column_1=($(cut -d "," -f 2 $file))
column_2=($(cut -d "," -f 3 $file))

echo "${column_0[@]}"

column_3=("column_3")

file_lines=$(cat $file | wc -l)

for ((i=1; i<$file_lines; i++));
do
	column_3[$i]=$((column_2[$i] - column_1[$i]))
done

echo "${column_3[@]}"

echo "${column_3[0]}" > column_3
for ((i=1; i<$file_lines; i++))
do
	echo "${column_3[$i]}" >> column_3
done

paste -d "," $file column_3 > report.csv
