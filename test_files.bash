#!/bin/bash

outputFile="./file_list.csv"

fileType="ELF"

for file in $(find / -type f);
do
	fileOut=$(file $file)
	if [[ "$fileOut" == *" ELF "* ]];
	then
		echo "\"$fileType\",\"$file\"" >> $outputFile
	fi
done
