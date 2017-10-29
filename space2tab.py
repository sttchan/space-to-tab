#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re
import os
import argparse


def convert_space(lines):
	new_lines = list()

	for line in lines:
	re_result, number = re.subn('\s+', '\t', line)
	new_lines.append(re_result)
	return new_lines


def main():
	usage = "Usage: " + sys.argv[0] + " -a [-o output_file_prefix] / -f input_file [-o output_file]\n"\
	+ "	-a : Process all files in current folder. \n" \
	+ "	-o : Output File Name , or Output File Prefix if '-a' flag specified. \n"\
	+ "	-f : Input File Name if '-a' flag not specified"

    # Check arguments
    if not (len(sys.argv) in (2, 3, 4, 5)):
	print("ERROR: Wrong Number of Arguments Provided")
	print(usage)	exit(1)

	flag_all_file = False
	flag_output_file = False
	flag_output_prefix = False

	# Get arguments
	arg_count = 1
	while arg_count < len(sys.argv):
	if sys.argv[arg_count] == '-a':
	flag_all_file = True
	elif sys.argv[arg_count] == '-o':
	if flag_all_file:
	output_file_prefix = sys.argv[arg_count+1]
	flag_output_prefix = True
	else:
	output_file_name = sys.argv[arg_count+1]
	flag_output_file = True
	arg_count += 1
	elif sys.argv[arg_count] == '-f':
	if flag_all_file:
	print("Ignoring input file name because \'-a\' flag.")	input_file_name = sys.argv[arg_count+1]	arg_count += 1
	arg_count += 1

	# build lists for input and output file

	if flag_all_file:
	input_file_names = list()
	output_file_names = list()
	for filename in os.listdir("./"):
	if not filename.startswith('.'):
	input_file_names.append(filename)
	output_file_names.append(filename)

	for count in range(len(output_file_names)):
	output_file_names[count] += "_tab.output"
	if flag_output_prefix:
	for count in range(len(output_file_names)):
	output_file_names[count] = output_file_prefix + "/" + output_file_names[count]
	else:
	input_file_names = input_file_name
	output_file_names = input_file_names
	if flag_output_prefix:
	output_file_names = output_file_prefix + "/" + output_file_names
	output_file_names += "_tab.output"

	# Read Lines

	if flag_all_file:
	for count in range(len(input_file_names)):
	try:
	with open(input_file_names[count], "r") as input_file:
	lines = input_file.read().splitlines()
	lines = "\n".join(convert_space(lines))

	except FileNotFoundError:
	print("Error: Input File \"" + input_file_names[count] + "\" not found.")
	print(usage)
	exit(1)

	# Write Lines
	try:
	with open(output_file_names[count], "w+") as outputFile:
	outputFile.writelines(lines)
	except FileNotFoundError:	print("Error: Output File \"" + output_file_names[count] + "\" not found.")
	print(usage)
	exit(1)

	print(input_file_names[count], '>>', output_file_names[count])
	else:	try:
	with open(input_file_names, "r") as inputFile:
	lines = inputFile.read().splitlines()	lines = "\n".join(convert_space(lines))

	except FileNotFoundError:
	print("Error: \"" + input_file_names + "\" not found.")
	print(usage)	exit(1)

	# Write Lines
	try:
	with open(output_file_names, "w") as outputFile:
	outputFile.writelines(lines)

	except FileNotFoundError:
	print("Error: \"" + output_file_names + "\" not found.")
	print(usage)	exit(1)

main()
