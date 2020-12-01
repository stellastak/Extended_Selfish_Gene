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

from collections import namedtuple
from typing import Sequence, Optional

from .utils import logging
from .base import Paranoid, Genotype, Tuple
from .fitness.base import Fitness


class Archive(Paranoid):
    """Archive of best solutions so far"""

    Element = namedtuple('Element', 'genotype fitness generation')

    def __init__(self):
        self._archive = set()
        self._age = 0

    def _add(self, genotype: Genotype, fitness: Fitness, generation: int) -> bool:
        """Add a new solution to Archive, return True if really added."""
        assert isinstance(
            genotype, Genotype), f"Only <Genotype, Fitness> can be added to the archive (genotype: {type(genotype)})"
        assert isinstance(fitness,
                          Fitness), f"Only <Genotype, Fitness> can be added to the archive (fitness: {type(fitness)})"

        new_element = Archive.Element(genotype, fitness, generation)
        if new_element in self._archive or any(ae.fitness >> fitness for ae in self._archive):
            return False
        else:
            new_set = {new_element}
            for old in self._archive:
                if not any(new.fitness >> old.fitness for new in new_set):
                    new_set.add(old)
            self._archive = new_set
            return True

    def add_generation(self, individuals: Sequence, generation: Optional[int] = None):
        """Add the individuals of a generation"""

        if generation is None:
            self._age += 1
            generation = self._age
        result = False
        for g, f in individuals:
            result = result or self._add(g, f, generation)
        return result

    @property
    def items(self):
        return list(self._archive)

    @property
    def age(self):
        return self._age

    @property
    def last_improvement(self):
        return max(a for _, _, a in self._archive)

    @property
    def first_improvement(self):
        return min(a for _, _, a in self._archive)

    def __iadd__(self, individuals) -> bool:
        """Add a set of individuals as a new generation."""
        return self.add_generation(individuals)

    def __len__(self):
        return len(self._archive)

    def __bool__(self):
        return bool(self._archive)

    def __iter__(self):
        return iter([e for e in self._archive])

    def run_paranoia_checks(self) -> bool:
        return True
