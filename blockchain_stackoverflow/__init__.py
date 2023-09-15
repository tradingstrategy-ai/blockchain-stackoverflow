"""Helper functions.

Shared across notebooks.
"""

import logging
import os

import matplotlib
import matplotlib.font_manager as font_manager


def load_matplotlib_local_fonts():

    # https://stackoverflow.com/a/69016300/315168
    font_path = os.path.join(os.path.dirname(__file__), 'Humor-Sans.ttf')
    assert os.path.exists(font_path)
    font_manager.fontManager.addfont(font_path)
    prop = font_manager.FontProperties(fname=font_path)

    matplotlib.rc('font', family='sans-serif') 
    matplotlib.rcParams.update({
        'font.size': 16,
        'font.sans-serif': prop.get_name(),
    })
    


def entertain_me():
    """Load our font and disable missing fonts warnings."""

    # https://stackoverflow.com/a/58393562/315168
    logging.getLogger('matplotlib.font_manager').disabled = True

    # Plot larger
    matplotlib.rcParams['figure.figsize'] = (12, 12)

    load_matplotlib_local_fonts()

    # Disable scientific notation on axes
    # https://stackoverflow.com/a/28373421/315168
    matplotlib.rcParams["axes.formatter.limits"] = (-99, 99)

    # English decimal separator
    matplotlib.rcParams["axes.formatter.use_locale"] = True

    # Matplotlib developer interface and memory management are unideal
    # https://stackoverflow.com/questions/27476642/matplotlib-get-rid-of-max-open-warning-output
    matplotlib.rcParams.update({'figure.max_open_warning': 0})
    
