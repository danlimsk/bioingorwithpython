### Example 6-2: Using the Unix sort command to sort a file

"""Produce a file of enzyme names and cut sites from the Rebase bionet file with
prototypes omitted and ^s removed, sorted by recognition site sequences"""

import os.path
import subprocess

def sort_bionet_file(filename = '../data/rebase-bionet-format.txt'):
    cleanfilename = write_clean(filename)
    sortedfilename = cleanfilename[:cleanfilename.rfind('.')] + '.sorted'
    # Construct Unix sort command
    # args = '-f -k 2 -b -o ' + sortedfilename + ' ' + cleanfilename
    # args = ' -l ' + sortedfilename + ' ' + cleanfilename
    # subprocess.call(('ls', '-l -t', sortedfilename, cleanfilename))
    # # tell Unix to execute the command
    # subprocess.call(('sort', '-f', '-k', '2', '-b', '-o', sortedfilename, cleanfilename))
    # subprocess.call('sort', '-f', '-k', '2', '-b', '-o', sortedfilename, cleanfilename)
    # subprocess.call('sort', ' -f -k 2 -b -o ', sortedfilename, cleanfilename)
    command = ('sort -f -k 2 -b -o ' + sortedfilename + ' ' + cleanfilename)
    subprocess.call(command, shell=True)       # tell Unix to execute the command


def write_clean(infilename):
    """Write a copy of file named infilename with prototypes and ^s
    omitted"""
    extpos = infilename.rfind('.')
    outfilename = ((infilename if extpos < 0 else infilename[:extpos]) +
                   '.clean')
    with open(infilename) as infile, open(outfilename, 'w') as outfile:
            write_clean_lines(infile, outfile)
    return outfilename

def clean_line(line):
    """Return line without its prototype (if any) and ^ (if any)"""
    line = line.replace('^', '')
    lpos = line.find('(')
    if lpos >= 0:
        rpos = line.find(')')
        return line[:lpos] + ' '*(rpos - lpos + 1) + line[rpos+1:]
    else:
        return line

def write_clean_lines(infile, outfile):
    for n in range(11):
        line = infile.readline()                 # skip first 10 lines (introduction)
    while len(line) > 1:                         # stop at empty line or end of file
        outfile.write(clean_line(line))
        line = infile.readline()

if __name__ == '__main__':
    sort_bionet_file()
