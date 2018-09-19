#!/usr/bin/env python3
### Demonstration ofuse of CodonUsageHistogram class in ch11_plot_histograms.py
### Code not in book Examples

from tkinter import *
from ch11_histogram_plot import CodonUsageHistogram
from ch11_get_usage_data import get_usage_data

tklist = []
def close_all():
    for tk in tklist:
        try:
            print(tk.title())
            tk.destroy()
        except:
            pass

def chart_usage(tk, name, outputdir=None):
    data = get_usage_data(name)
    if not data:
        print(name, 'not found in database')
        return
    CodonUsageHistogram(tk, name, data, outputdir)

def chart_usages(names, outputdir=None):
    for name in names:              # usually only 1
        print(name, file=sys.stderr)
        tk = Tk()
        tklist.append(tk)
        tk.title(name)
        frame = Frame(tk)
        frame.pack()
        chart_usage(tk, name)
    try:
        sys.ps1                     # are we running interactively?
    except:                         # no
        input("Press the Return key to close the window(s)")


default_names = (
    'Acidobacterium capsulatum',
    'Sulfolobus acidocaldarius',
    'Sulfolobus acidocaldarius DSM 639',
    'Streptococcus thermophilus',
    'Geobacillus stearothermophilus',
    'Bacillus subtilis',
    'Thermotoga maritima',
    'Thermus thermophilus',
    'Pseudomonas viridiflava',
    'Bordetella parapertussis',
    'Haemophilus influenzae',
    'Sporosarcina pasteurii',
    'Helicobacter pylori',
    )

if __name__ == '__main__':
    outputdir = 'output'
    if len(sys.argv) == 1:          # no args
        names = default_names[-2:]
    elif len(sys.argv) == 2:         # regexp
        pat = re.compile(sys.argv[1], re.I)
        names = [name for name in default_names if pat.search(name)]
        if not names:
            if len(sys.argv) == 2:
                print('no default names match', repr(sys.argv[1]))
    else:                           # first against each of the others
        names = ' '.join([sys.argv[1].title()] +
                         [arg.lower() for arg in sys.argv[2:]])

    chart_usages(names, outputdir)
