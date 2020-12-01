# -*- coding: utf-8 -*-
#############################################################################
#   _________ ____________  ___                                             #
#  /   _____//  _____/\   \/  /  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #
#  \_____  \/   \  ___ \     /   THE E(X)TENDED (S)ELFISH (G)ENE ALGORITHM  #
#  /        \    \_\  \/     \   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #
# /_________/\________/___/\  \  https://github.com/squillero/sgx           #
#                           \_/                                             #
#                                                                           #
# A quick 'n dirty versatile population-less evolutionary optimizer loosely #
# inspired by a cool interpretation of the Darwinian theory.                #
#                                                                           #
#############################################################################

# Copyright 2020 Giovanni Squillero
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import warnings
from .cpu_time import microgp4_process_time

DefaultLogger = logging.getLogger('sgx')

# Propagate Log levels, and add a few ones
SPAM = logging.DEBUG - 1
DEBUG = logging.DEBUG
VERBOSE = logging.INFO - 1
INFO = logging.INFO
BARE = logging.INFO + 1
CRITICAL = logging.CRITICAL
WARNING = logging.WARNING
ERROR = logging.ERROR

# Setup DefaultLogger's handler
DefaultLogger.handler = list()
DefaultLogger.setLevel(logging.INFO)
DefaultLogger.__doc__ = "Default MicroGP4 logger"


def log_cpu(level: int = INFO, msg: str = "", *args, **kwargs) -> None:
    """Like log(), but including cpu time."""
    if msg:
        DefaultLogger.log(level, "%s: %s", msg, microgp4_process_time())
    else:
        DefaultLogger.log(level, "%s", msg, microgp4_process_time())


def log_split(level: int, msg: str) -> None:
    for line in msg.split("\n"):
        DefaultLogger.log(level, line)


DefaultLogger.log_cpu = log_cpu
DefaultLogger.log_split = log_split

# Log SPAM, VERBOSE & BARE
DefaultLogger.spam = lambda *args, **kwargs: DefaultLogger.log(SPAM, *args, **kwargs)
DefaultLogger.verbose = lambda *args, **kwargs: DefaultLogger.log(VERBOSE, *args, **kwargs)
DefaultLogger.bare = lambda *args, **kwargs: DefaultLogger.log(BARE, *args, **kwargs)

# shortcuts
spam = DefaultLogger.spam
debug = DefaultLogger.debug
verbose = DefaultLogger.verbose
info = DefaultLogger.info
warning = DefaultLogger.warning
error = DefaultLogger.error
critical = DefaultLogger.critical
bare = DefaultLogger.bare
set_level = lambda *args, **kwargs: DefaultLogger.setLevel(*args, **kwargs)

try:
    import coloredlogs

    logging.addLevelName(SPAM, ' SPAM')
    logging.addLevelName(DEBUG, ' DEBUG')
    logging.addLevelName(VERBOSE, ' VERBOSE')
    logging.addLevelName(INFO, ' INFO')
    logging.addLevelName(BARE, '')
    logging.addLevelName(WARNING, ' WARNING')
    logging.addLevelName(ERROR, ' ERROR')
    logging.addLevelName(CRITICAL, ' CRITICAL')
    coloredlogs.install(level='INFO',
                        logger=DefaultLogger,
                        fmt='%(asctime)s%(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        field_styles={
                            'asctime': {
                                'color': 'cyan'
                            },
                            'levelname': {
                                'color': 'blue',
                                'bold': False,
                                'bright': True
                            }
                        },
                        level_styles={
                            logging.getLevelName(ERROR): {
                                'color': 'red',
                                'bold': True
                            },
                            logging.getLevelName(CRITICAL): {
                                'color': 'red',
                                'bold': True
                            },
                            logging.getLevelName(WARNING): {
                                'color': 'yellow',
                                'bold': True
                            },
                            logging.getLevelName(DEBUG): {
                                'color': 'black',
                                'bright': True
                            },
                            logging.getLevelName(SPAM): {
                                'color': 'black',
                                'bright': True
                            }
                        })
except:
    WARN_NOCOLOR = "Colored log not available (install module 'coloredlogs')."
    warnings.warn(WARN_NOCOLOR, RuntimeWarning)
    logging.addLevelName(SPAM, ' [SPAM]')
    logging.addLevelName(DEBUG, ' [DEBUG]')
    logging.addLevelName(VERBOSE, ' [VERBOSE]')
    logging.addLevelName(INFO, ' [INFO]')
    logging.addLevelName(BARE, '')
    logging.addLevelName(WARNING, ' [WARNING]')
    logging.addLevelName(ERROR, ' [ERROR]')
    logging.addLevelName(CRITICAL, ' [CRITICAL]')
    logging.basicConfig(level='DEBUG', format='%(asctime)s%(levelname)s %(message)s', datefmt='%H:%M:%S')
