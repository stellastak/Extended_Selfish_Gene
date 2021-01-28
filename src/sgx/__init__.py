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

"""The eXtended Selfish Gene algorithm (SGX):
A population-less EA loosely inspired by a cool interpretation of the Darwinian theory.
See: https://github.com/squillero/sgx

Copyright © 2021 Giovanni Squillero. Licensed under Apache-2.0.
"""

__title__ = "Extended Selfish Gene (SGX)"
__name__ = "Extended Selfish Gene (SGX)"
__version__ = "0.2.dev2"
__author__ = "Giovanni Squillero", "Alberto Tonda"
__copyright__ = "Copyright (c) 2021 Giovanni Squillero. Licensed under Apache-2.0."

import sys
import warnings


sys.stderr.flush()
sys.stdout.flush()

if sys.flags.optimize == 0:
    warnings.warn("All debug checks are active, performances are significantly impaired.", RuntimeWarning, stacklevel=2)

if sys.version_info < (3,):
    sys.exit(
        f"{__name__} v{__version__} is not compatible with Python {sys.version_info.major}.{sys.version_info.minor}")

if sys.version_info < (3, 6):
    warnings.warn(
        f"Python version 3.6 or later is required " +
        "({__name__} v{__version__} has not been tested with Python {sys.version_info.major}.{sys.version_info.minor})",
        Warning,
        stacklevel=2)

sys.stderr.flush()
sys.stdout.flush()

