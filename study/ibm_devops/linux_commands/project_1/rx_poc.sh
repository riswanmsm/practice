#!/bin/bash

# storing a file name for save the downloaded data in a variable
file_name="raw_data_"$(date "+%Y%m%d")
# storing the city which we are going to download weather data in a variable
city=Casablanca

# download the weather data and output in the already defined file
curl wttr.in/$city >  $file_name

# take only lines which are having temperature with °C and outputting in a text file
grep  °C $file_name > temperatures.txt

# take the first line of the text file fro current temperature,
# split the line to get the temperature in numerical
obs_tmp=$(cat -A temperatures.txt | head -1 | cut -d ";" -f7 | cut -d "^" -f1 | cut -d "m" -f2)
fc_tmp=$(cat -A temperatures.txt | head -3 | tail -1 | cut -d "+" -f3 | cut -d "^" -f1)

export TZ="Morocco/Casablanca"

# Store the current hour, day, month and year in a variable using - as seperator
current_date_time=$(date "+%H-%d-%m-%Y")
current_hour=$(echo $current_date_time | cut -d '-' -f1)
# Store the current day in a variable
current_day=$(echo $current_date_time | cut -d '-' -f2)
# Store the current month in a variable
current_month=$(echo $current_date_time | cut -d '-' -f3)
# Store the current year in a variable
current_year=$(echo $current_date_time | cut -d '-' -f4)

# append data date time record to the log file named rx_proc.log
# touch rx_proc.log;header="year\tmonth\tday\thour\tobs_tmp\tfc_tmp";
data="$current_year\t$current_month\t$current_day\t$current_hour\t$obs_tmp\t$fc_tmp"
echo -e $data >> rx_poc.log


