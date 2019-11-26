""" Module to manage logs """
from datetime import datetime


class VerboseLevel(object):
    NORMAL = 3


current_verbose_level = VerboseLevel.NORMAL
log_file = "log.txt"
show_datetime = True


def showlogconsole(log_message):
    """
    Show log on console
    """
    print(log_message)


def savelogfile(log_message):
    """
    Save log into file
    """
    with open(log_file, 'a+') as file_handler:
        file_handler.write(log_message + "\n")


def log(log_message, verbose_level=3):
    """
    Show log on console
    """
    global log_buffer

    if verbose_level is None:
        verbose_level = current_verbose_level

    if show_datetime:
        log_message = str(datetime.now()) + ": " + str(log_message)
    if verbose_level <= current_verbose_level:
        log_function(log_message)


# Set current function to be used as log
# Current options:
#   - showlogconsole
#   - savelogfile
log_function = showlogconsole
