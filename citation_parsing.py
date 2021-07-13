#!/usr/local/bin/python3.7

'''
This file takes in an Rmd file and parses out the number of times
each citation is used in the file. Uses regex to find the citations after @ symbol,
if any emails or anything using '@' symbol in file is to be ignored, user
can specify it as well. Outputs a csv file containing counts of each citation.
'''

'''
Requires python 3.7, re module, pandas module, and csv module.
'''
import getopt
import sys
import re
import pandas as pd
import csv


def main(argv):
    print(sys.argv[1:])
    rmdfile = ''
    ignore = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hr:o:i:", ["rfile=","ofile=" "ifile="])
    except getopt.GetoptError as err:
        print('citation_parsing.py -r <rmdfile> -o <outputfile> -i <ignore>')
        print(err)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('citation_parsing.py -r <rmdfile> -o <outputfile> [-i <ignore>]',
                  '\n **This script allows you to determine how many times each citation is used in a R markdown file. '
                  ,'Outputs a csv file containing the counts of each citation.**',
                  '\n **Requires: Requires python 3.9, re module, pandas module, and csv module.',
                  '\n **Required Arguments:**', '\n \t -r <rmdfile> : R Markdown file that will be parsed for citations'
                  '\n \t -o <outputfile> : Desired name of output csv file with extension ".csv" .',
                  '\n **Optional Arguments:**','\n \t -i <ignore> : list of any strings the user would like the program to ignore, '
                                               'possible example could be email addresses. Must be in the format of '
                                               ' "ignore_word ignore_word", with the ignore words as one string '
                                               'surrounded by quotations and each ignore word separated by spaces.  ')
            sys.exit()
        elif opt in ("-r", "--rfile"):
            rmdfile = arg
        elif opt in ("-i", "--ifile"):
            ignore = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print('Rmd file is ', rmdfile)
    print('Output file is ', outputfile)
    print('Ignore list is ', ignore)
    # Dictionary to hold the counts of each citation
    counts = {}
    # List of emails or other strings user does not want to count as a citation
    # Regex pattern
    regex = r"(@{1}.*?)(;|])"
    ignore_list = ignore.split(' ')

    # Read in Rmd file
    with open(rmdfile, 'r') as rmd:
        # Go line by line in the rmd file
        for line in rmd:
            # find any matches to the regex
            matches = re.finditer(regex, line, re.MULTILINE)
            # if there are any matches (matches will not be None)
            if matches:
                # iterate through all the matches in the line
                for match in matches:
                    # extract the citation
                    citation = match.groups()[0]
                    # if the citation is not in the dictionary already and it is not in the user specified list of
                    # @ character symbols not to use, then add it to the counts dictionary
                    if ignore_list:
                        if citation not in counts and citation not in ignore_list:
                            counts[citation] = 1
                        # else add one to the counts for the citation
                        else:
                            counts[citation] += 1
                    else:
                        if citation not in counts:
                            counts[citation] = 1
                            # else add one to the counts for the citation
                        else:
                            counts[citation] += 1

    with open(outputfile, 'w') as output:
        writer = csv.writer(output)
        for key, value in counts.items():
            writer.writerow([key, value])


if __name__ == "__main__":
    main(sys.argv[1:])


