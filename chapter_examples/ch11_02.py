### Example 11-2: A subclass for testing an abstract class

from ch11_plot import Plot

if __name__ == '__main__':

    class EmptyPlot(Plot):
        canvas_background = 'gray90'
        def get_plot_dimensions(self):
            return 200, 150, 20, 20, 10, 10
        def draw_plot(self):
            self.draw_line(0, 0, 100, 100)

    plot = None
    try:
        plot = EmptyPlot()
        plot.execute()
        input(
'''You should see a light-gray plot with a line
from (0,0) to (100,100); press Return to close ''')
    finally:
        if plot:
            plot.close()
