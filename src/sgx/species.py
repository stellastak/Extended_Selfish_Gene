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

from typing import Tuple, Sequence, Any, Callable, Optional, Hashable, Union

from .utils import logging
from .fitness import FitnessFunction
from .utils.random import SGxRandom
from .base import Genome, Genotype
from .allele.base import Allele
from .fitness.base import Fitness


class Species:
    """Missing"""

    def __init__(self,
                 genome: Sequence[Any],
                 fitness_function: FitnessFunction,
                 mutation_rate: Optional[float] = None) -> None:

        self._genome = Genome(genome)
        self._fitness_function = fitness_function

        if mutation_rate is None:
            self._mutation_rate = 1 / len(self._genome)

    @property
    def genome(self) -> Genome:
        return self._genome

    @property
    def fitness_function(self) -> FitnessFunction:
        return self._fitness_function

    def sample(self, sample_type: Optional[str] = Allele.DEFAULT_SAMPLE_TYPE) -> Genotype:
        """Sampling the genotypes with a specific method.

        Args:
            sample_type: The type of sampling is going to be used.

        Returns:
            The candidate's Genotype after sampling.
        """
        genotype = list()
        for a in self._genome:
            if SGxRandom.random() < self._mutation_rate:
                genotype.append(a.sample(sample_type='uniform'))
            else:
                genotype.append(a.sample(sample_type='sample'))
        return Genotype(genotype)

    def update(self, winner: Genotype, loser: Genotype):
        """Updates the winner and the loser Genotype, so as to modify the new Learning Rate.

        Args:
            winner: The genotype of the better solution.
            loser: The genotype of the worse solution.
        """
        for a, w, l in zip(self._genome, winner, loser):
            a.update(winner=w, loser=l)

    def evaluate(self, genotype: Genotype) -> Fitness:
        """Evaluates a genotype according to a specific Fitness Function.

        Args:
            genotype: The Genotype which is going to be evaluated.

        Returns:
            The fitness calculated from a Fitness Function.
        """
        return self._fitness_function(genotype)
