# Set version

__version__ ="0.2.13"

# Logger config
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
sh = logging.StreamHandler()
sh.setFormatter(logging.Formatter('PandasGUI %(levelname)s — %(name)s — %(message)s'))
logger.addHandler(sh)

# Imports
from pandasgui.gui import show

__all__ = ["show", "__version__"]
