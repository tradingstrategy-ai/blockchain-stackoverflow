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
    matplotlib.rcParams['figure.figsize'] = (15, 15)

    load_matplotlib_local_fonts()
