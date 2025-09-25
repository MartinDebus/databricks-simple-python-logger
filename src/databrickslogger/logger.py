import logging
import sys

class DatabricksLogger(logging.Logger):
    """
    A custom logger class that extends logging.Logger to facilitate    
    logging with configurable log levels using string inputs. 

    The logs will be directed to the stdout destination. Make sure to
    redirect cluster logs of the Databricks Cluster to a Volume for      
    later use.

    This class allows users to set the logging level using strings, 
    abstracting the need to import and use the logging module directly.

    Parameters
    ----------
    name : str
        The name of the logger.
    level : str, optional
        The logging level as a string (e.g., 'DEBUG', 'INFO'). 
        Default is 'DEBUG'.

    Attributes
    ----------
    _LOG_LEVELS : dict
        A dictionary mapping string representations of log levels to 
        their corresponding logging level constants.
    """

    # Define a mapping of level names to logging levels
    _LOG_LEVELS = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR,
        'CRITICAL': logging.CRITICAL
    }

    def __init__(self, name, level='DEBUG'):
        """
        Initialize the DatabricksLogger with a specified name and
        logging level.

        Parameters
        ----------
        name : str
            The name of the logger.
        level : str, optional
            The logging level as a string (e.g., 'DEBUG', 'INFO'). 
            Default is 'DEBUG'.
        """
        # Map the string level to the corresponding logging level 
        # constant
        log_level = self._LOG_LEVELS.get(level.upper(), logging.DEBUG)
        super().__init__(name, log_level)
        self._setup_logging(log_level)

    def _setup_logging(self, level):
        """
        Set up the logging configuration with the specified level.

        Parameters
        ----------
        level : int
            The logging level constant from the logging module.
        """
        handler = logging.StreamHandler(sys.stdout)
        formatter = (
            logging
                .Formatter(
                    '%(name)s|%(asctime)s|%(levelname)s|%(message)s'
                )
        )
        handler.setFormatter(formatter)

        # prevent duplicate handlers
        if not any(
            isinstance(h, logging.StreamHandler) and h.stream == sys.stdout
            for h in self.handlers
        ):
            self.addHandler(handler)

        self.setLevel(level)