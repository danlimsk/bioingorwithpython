### Example 11-4: Test code for the DotPlot module

from random import randint
from ch11_dotplot import DotPlot

aacodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M',
           'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

def generate_sequence(length):
    return ''.join([aacodes[randint(0, len(aacodes)-1)]
                   for n in range(length)])

if __name__ == '__main__':
    string = generate_sequence(202)
    plot = DotPlot(string, string, window=3, threshold=2, with_axes=True)
    plot.execute()                                      # defined in Plot
    try:
        sys.ps1                                         # are we running interactively?
    except:                                             # no
        input("Press the Return key to close the window(s)")
        plot.close()
