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

from abc import ABC, abstractmethod

from ..utils import logging
from ..utils.random import SGxRandom
from .simple import Vector


class MultiObjective(Vector, ABC):
    """Abstract class for handling Multi-Objective problems."""

    @abstractmethod
    def is_fitter(self, other: 'Lexicase') -> bool:
        raise NotImplementedError

    def is_dominant(self, other: 'Lexicase') -> bool:
        self.check_comparable(other)
        return all(f1 >= f2 for f1, f2 in zip(self._values, other._values)) and any(
            f1 > f2 for f1, f2 in zip(self._values, other._values))


class Lexicase(MultiObjective):
    """Pseudo-MO through Lexicase selection (DOI:10.1109/TEVC.2014.2362729)."""

    def is_fitter(self, other: 'Lexicase') -> bool:
        self.check_comparable(other)
        order = SGxRandom.shuffled(range(len(self._values)))
        return Vector.compare_vectors([self._values[i] for i in order], [other._values[i] for i in order]) > 0
