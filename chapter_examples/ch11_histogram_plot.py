#!/usr/bin/env python3

from tkinter import *

import re

import ch11_get_usage_data as usage
from ch11_plot import Plot

class CodonUsageHistogram(Plot):

# Fields that override inherited values
    x_tic_length = y_tic_length = 16

# Fields specific to this class
    barwidth = 10                   # width of histogram bars
    barspacing = 5                  # spacing of histogram bars
    barscale = 3                    # vertical pixels per data point
    codon_font_size = 14
    marker_font_size = 14
    title_font_size = 22
    key_font_size = 16
    codon_faces = ('Liberation Mono Regular',
                   'Lucida Sans Typerwriter',
                   'DejaVu Sans Mono',
                   'Bitstream Sans Mono',
                   'Courier')
    gc_colors = ('gray80', 'gray60', 'gray40', 'gray25')
    default_bar_color = 'gray94'
    plot_top_margin = 20
    ylabel_width = 60
    xlabel_height = codon_font_size*5
    canvas_background = 'white'
    title_pad_y = 6
    key_pad_y = 12

    codons = [base1 + base2 + base3
              for base1 in 'TCAG'
              for base2 in 'TCAG'
           for base3 in 'TCAG']
    codon_labels = codons[:]        # a copy to modify
    startchar = '*'
    altstartchar = "'"
    stopchar = '^'
    gc_colors = ('gray80', 'gray60', 'gray40', 'gray25')
    # add start and stop indicators
    # stop codons:
    for codon in ('TAA', 'TAG', 'TGA'):
        codon_labels[codon_labels.index(codon)] += stopchar
    # standard start codon:
    codon_labels[codon_labels.index('ATG')] = 'ATG' + startchar
    # alternate start codons in code 11
    for codon in ('TTG', 'CTG', 'GTG', 'ATT', 'ATA', 'ATC'):
        codon_labels[codon_labels.index(codon)] += altstartchar

    def __init__(self, name, data,
                 # super paramaters:
                 windowtitle=None, scale=1.0,
                 ps_filename=None,  ps_scale = 1.0):
        self.data = dict(data)
        self.name = name
        super().__init__(name, scale, ps_filename, ps_scale)

    def setup_fonts(self):
        super().setup_fonts()
        self.add_font('x', self.findfont(self.codon_faces,
                                         self.codon_font_size,
                                         True))
        self.add_font('title', self.findfont(self.sans_faces,
                                             self.title_font_size,
                                             True))
        self.add_font('key', self.findfont(self.sans_faces,
                                              self.key_font_size,
                                              False, True))
        self.add_font('marker', self.get_font('x').copy())
        self.get_font('marker').configure(size=self.marker_font_size)
        self.add_font('species', self.get_font('title').copy())
        self.get_font('species').configure(slant='italic')

    def setup_data(self):
        self.maxval = max(self.data.values())
        self.sumval = sum(self.data.values())
        self.maxpercent = round((100 * self.maxval) / self.sumval)

    def get_plot_dimensions(self):  # required
        dims = (self.barspacing + round(64 * self.scale *
                                        (self.barwidth + self.barspacing)),
                round(self.scale * self.barscale * (2 + self.maxval)),
                self.ylabel_width + 20,
                20,
                self.get_title_height(),
                self.xlabel_height + self.get_key_height()
                )
        return dims

    def get_title_height(self):
        return 2 * self.title_font_size

    def get_key_height(self):
        return 2 * self.key_font_size

    def draw_y_tics(self):
        for n in range(1, self.maxpercent + 1):
            vertpos = 10 * n * self.barscale
            # * 10 because barheights are per thousand
            self.draw_line(0, vertpos, -self.y_tic_length, vertpos)

    def draw_y_axis_labels(self):
        for n in range(1, self.maxpercent + 1):
            self.draw_text(-self.y_tic_length-4,
                            10 * n * self.barscale,
                            str(n) + '%',
                            'y',
                            anchor='e')

    def draw_x_axis_labels(self):
        curx = self.barspacing + 5
        for n, codon in enumerate(self.codon_labels):
            self.draw_codon_label(curx, codon),
            curx += self.barwidth + self.barspacing

    def draw_codon_label(self, x, codon):
        for n, char in enumerate(codon):
            self.draw_text(x,
                           # 6 * is additional separation for markers
                            -((self.codon_font_size * (n+1)) +
                              (6 * (n > 2))),
                           char,
                           'x' if n < 3 else 'marker',
                           anchor='center')

    def draw(self):
        super().draw()
        self.draw_title()
        self.draw_gc_content()
        self.draw_key()

    def draw_title(self):
        self.draw_text(round(self.plot_width / 2), self.plot_height,
                       'cDNA Codon Usage for ',  'title',  anchor='se')
        self.draw_text(round(self.plot_width / 2), self.plot_height,
                       self.name, 'species',  anchor='sw')

    def draw_gc_content(self):
        self.draw_text(20, self.plot_height-20,
                       'GC content = {:.2f}%'.format(self.gccontent()),
                       'key', 'sw')

    def draw_key(self):
        self.draw_text(
            0,  -self.xlabel_height,
            'Key to Genetic Code 11: ' +
            '{} start, {} possible start, {} stop'.
            format(self.startchar, self.altstartchar, self.stopchar),
            'key',  anchor='nw')
        self.draw_text(
            self.plot_width, -self.xlabel_height,
            'The more Gs and Cs a codon has the darker its bar.',
            'key', anchor='ne')

    @classmethod
    def codon_gc_count(self, codon):
        return codon.count('G') + codon.count('C')

    @classmethod
    def gccolor(self, codon):
        return self.gc_colors[self.codon_gc_count(codon)]

    def gccontent(self):
        # 3 because there are 3 bases in each codon
        # 10 because the counts are per thousand
        return (3 * 10 * sum((self.codon_gc_count(codon) * count
                          for codon, count in self.data.items())) /
                self.sumval
                )

    def draw_plot(self):            # required
        curx = self.barspacing
        for codon in self.codons:
            n = self.data[codon]
            self.draw_rectangle(curx,  0,  self.barwidth,  n * self.barscale,
                                self.gccolor(codon))
            curx += self.barwidth + self.barspacing

def validate_data(name, data, threshold):
    if data == []:
        raise Exception("Didn't find data for", name)
    elif data == None:
        raise Exception("Total of counts for ", name, "is too small")
    elif len(data) != 64:
        raise Exception(
            "Problem: length of data for {}\nis {} but should be 64"
            .format(name, len(data))
            )
    else:
        total = sum(data.values())
        if total < .9 * threshold or total > 1.1 * threshold:
            raise Exception("The sum of the counts isn't near the threshold")

def chart_usage(tk, name):
    data = usage.get_usage_data(name)
    if not data:
        print(name, 'not found in database')
        return
    CodonUsageHistogram(name, data).execute()

tklist = []
def close_all():
    for tk in tklist:
        try:
            print(tk.title())
            tk.destroy()
        except:
            pass

def chart_usages(names, outputdir=None):
    for name in names:              # usually only 1
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
    outputdir = '../data/Genbank/CodonUsage'
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
