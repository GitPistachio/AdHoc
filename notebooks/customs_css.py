"""customs_css: Custom css adjustments to a jupyter notebooks."""

__author__ = "Wojciech Raszka"
__copyright__ = "Copyright 2020, GitPistachio"
__version__ = "1.0"
__license__ = "BSD-3-Clause"
__email__ = "GitPistachio@gmail.com"


from IPython.core.display import HTML, display


class CCSS:
    """Set of custom CSS adjustments to a jupyter notebooks."""
    
    CENTER_PLOTS_CSS = """
        .output_png {
            display: table-cell;
            text-align: center;
            vertical-align: middle;
        }"""
        
    def centerPlots(self, silent=True):
        """Center all plots in notebook."""
        if not silent:
            print("All plot from now on will by align to the center.")
        display(HTML("<style>{}</style>".format(self.CENTER_PLOTS_CSS)))