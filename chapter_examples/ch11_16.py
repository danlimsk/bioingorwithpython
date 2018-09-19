### Example 11-16: Drawing a sequence trace using SVG polylines

colors = ('black', 'green', 'red', 'blue')            # or whatever
axiscolor = '#333'
axisthickness = 2

tickcolor = '#666'
tickspacing = 100                                     # spacing of x-axis labels
tickheight = 18
tickthickness = 2

maxval = 1600
leftmargin = 10
topmargin = 20
yzero = 100

hscale = 5/2                                          # multiply x coordinates by this
vscale = 14                                           # divide y values by this
span = 1                                              # number of points to average together

def read_data(infilname):
    with open(infilname) as infil:
        return [eval(line) for line in infil.readlines()]

def write_text(fil, x, y, txt, cls):
    print("  <text class='{}' x='{}' y='{}'>{}</text>".
          format(cls, x+leftmargin, y+topmargin, txt),
          file=fil)

def write_line(fil, frompos, fromval, topos, toval, color, thickness):
        print("  <line x1='{}' y1='{}' x2='{}' y2='{}'".
              format(leftmargin + int(frompos * hscale),
                     int(((maxval - fromval) / vscale)) + topmargin,
                     leftmargin + int(topos * hscale),
                     int(((maxval - toval) / vscale)) + topmargin),
              end=' ',
              file=fil),
        print("style='stroke: {}; stroke-width: {};'/>".
              format(color, thickness),
              file=fil)

def write_axes(fil, count):
    print(file=fil)
    write_line(fil, 0, 0, 0, maxval, axiscolor, axisthickness)
    write_line(fil, 0, 0, count, 0, axiscolor, axisthickness)
    print(file=fil)
    tickbottom = vscale * (-axisthickness - tickheight)
    for x in range(int(tickspacing / hscale),
                   count,
                   int(tickspacing // hscale)):
        write_line(fil, x, tickbottom + vscale * (1 + tickheight), x, tickbottom,
                   tickcolor, tickthickness)
        write_text(fil,
                   int(x * hscale),
                   int((maxval / vscale)) + tickheight + 15,
                   int(x * hscale),
                   'tick')

def write_bases(outfil, start, bases, positions):
    for base, pos in zip(bases, positions):
        write_text(outfil,
                   int(pos * hscale - 3),
                   int((maxval / vscale)) + 15,
                   base,        # text
                   base)        # class
    # - to "center" the base at its position; just a guess
    print(file=outfil)

def print_point(outfil, x, y):
    print("{},{}".format(leftmargin + int(x * hscale),
                           int((maxval - y) / vscale) + topmargin),
          file=outfil,
          end=' '
          )

def write_curve(outfil, vals, color):
    # at a point in the curve instead of using every data point
    # hscale is how far apart the x points are
    print("""
  <polyline style='fill: none; stroke: {}; stroke-width: 1;'
            points='""".
          format(color),
          file=outfil,
          end=''),

    # span is a file-level parameter that specifies the number of points to average to compute
    # a value rather than having a value for every point on the x axis; blur does the averaging
    for pos in range(0, len(vals)-1, span):
        if not pos % 6:                                          # 5-digit x's at the end
            print(20*' ', file=outfil, end='')
        print_point(outfil, pos/span, blur(vals[pos:pos+span]))

    print("  ' />", file=outfil)                                 # close polyline

def write_curves(outfil, data,):
    for d, clr in zip(data, colors):
        write_curve(outfil, d, clr)

def blur(seq):
    """return the average of the values in seq"""
    return 0 if not seq else sum(seq)/len(seq)

def write_heading(outfil, width, height):
    print(
"""<?xml version="1.0" standalone="no"?>

<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<svg xmlns='http://www.w3.org/2000/svg' version='1.1'
     width='{0}' height='{1}'
>""".format(width+(2*leftmargin), height+yzero+20),
"""
  <defs>
    <style type='text/css'><![CDATA[
        text {
              font-family: Futura, 'Andale Mono', Verdana, sans-serif;
              fill:black;
              font-weight: normal;
              font-size: 8pt;
              font-style: normal;
              text-rendering:optimizeLegibility;
            }
        text.tick { }
        text.T { fill: red; }
        text.C { fill: blue; }
        text.A { fill: green; }
        text.G { fill: black; }
      ]]>
    </style>
  </defs>
""",  file = outfil, end='\n')

def write_closing(outfil):
    print('\n</svg>', file = outfil)

def write_svg_file(infilname, outfilname):
    data = read_data(infilname)
    start = data[0]
    bases = data[1]
    positions = data[2]
    values = data[3:]
    with open(outfilname, 'w') as outfil:
        write_heading(outfil, len(values[0]) // span, maxval // vscale)
        write_axes(outfil, len(values[0]) // span)
        write_bases(outfil, start, bases, positions)
        write_curves(outfil, values)
        write_closing(outfil)

write_svg_file('../data/seqdata', '../data/abi-trace.svg')

import webbrowser
import os.path
webbrowser.open('file://' + os.path.realpath('../data/abi-trace.svg'))
