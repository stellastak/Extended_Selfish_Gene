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

from typing import Callable, Any, Optional, Type
from collections import abc
import warnings

from .base import Fitness
from .simple import Scalar
from ..base import Genotype
from ..utils import logging


class FitnessFunction(abc.Callable):
    #    def __init__(self, fitness_function: Callable[[Genotype], Fitness], type_: Optional[Fitness.__class__] = Scalar.__class__, best_fitness: Optional[Fitness] = None):
    def __init__(self,
                 fitness_function: Callable[[Genotype], Any],
                 type_: Optional[Type[Fitness]] = Type[Scalar],
                 best_fitness: Optional[Fitness] = None):
        self._fitness_function = fitness_function
        self._fitness_type = type_
        self._best_fitness = type_(best_fitness)

    def __call__(self, genotype: Genotype) -> Fitness:
        return self._fitness_type(self._fitness_function(genotype))

    @property
    def fitness_type(self):
        return self._fitness_type

    @property
    def best_fitness(self):
        return self._best_fitness
