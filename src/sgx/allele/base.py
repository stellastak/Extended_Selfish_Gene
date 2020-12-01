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

from typing import Tuple, Optional, Hashable
from abc import ABC, abstractmethod

from ..utils import logging
from ..base import Paranoid, Pedantic


class Allele(Paranoid, Pedantic, ABC):
    """Abstract class for Allele/

    An allele must be Hashable (ie. non modifiable)
    """

    SAMPLE_TYPE__SAMPLE = 'sample'
    SAMPLE_TYPE__UNIFORM = 'uniform'
    SAMPLE_TYPE__MODE = 'mode'
    VALID_SAMPLE_TYPES = [SAMPLE_TYPE__SAMPLE, SAMPLE_TYPE__MODE, SAMPLE_TYPE__UNIFORM]
    DEFAULT_SAMPLE_TYPE = SAMPLE_TYPE__SAMPLE

    @property
    def mode(self) -> Hashable:
        return self.sample(sample_type='mode')

    @property
    def possible_values(self) -> Optional[Tuple[str]]:
        """Possible values of the allele. None if not reasonably applicable (eg. a float)"""
        return None

    @abstractmethod
    def sample(self, sample_type: Optional[str] = DEFAULT_SAMPLE_TYPE) -> Hashable:
        """Sample.

        sample_type:
            'sample' (default): random value according to the current probability distribution
            'uniform': random value according to a uniform probability distribution (ie. completely random)
            'mode': most common value according to the current probability distribution
        """
        pass

    @abstractmethod
    def update(self, winner: Hashable, loser: Hashable) -> None:
        pass

    @abstractmethod
    def describe(self) -> str:
        """Pretty describe the current allele"""
        return '*undef*'

    def __str__(self) -> str:
        return f'⟪{self.describe()}⟫'

    @property
    def is_squeezable(self) -> bool:
        if self.possible_values is None:
            return False
        return all(len(str(v)) == 1 for v in self.possible_values)
