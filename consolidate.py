#!/usr/bin/python
# consolidate.py
# author: zimpos

# Creates a flat file of all Yara signatures (for loading into LaikaBOSS or similar) according to the index.yar file
# NOTE: for python3.x

import os, re

## get list of yara indexes
#ignore = ["Mobile_Malware"]
#directory = "."
#
#ls = filter(lambda x: "_index.yar" in x, (os.listdir(directory)))
#index = 0
#
#for d in ls:
#	if ("{}_index.yar".format(d))in ignore:
#		del ls[index]
#
#	index += 1

# write to file
infile = open("index.yar")
outfile = open("signatures.yara", "w+")

rexp = re.compile("include\s\"(.+)\"")

for line in infile:
	match = re.search(rexp, line) 
	if match:
		f = open(match.group(1), "r")

		for line in f:
			outfile.write(line)		
