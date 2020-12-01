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

from typing import Sequence, Any, Optional, Tuple
import random


class Random:

    def __init__(self, seed: Optional = None, state: Optional[Tuple] = None):
        assert not (seed and state), "Can't set both seed and state"
        self._random = random.Random()
        if state:
            self._random.setstate(state)
        else:
            self._random.seed(seed)

    def random(self) -> float:
        """Return a random value in the interval [0, 1)."""
        return self._random.random()

    def choice(self, population: Sequence[Any], weights: Optional[Sequence[float]] = None) -> Any:
        """Return a random element from a non-empty population with optional relative weights."""
        return self._random.choices(population, weights=weights, k=1)[0]

    def shuffled(self, population: Sequence[Any]) -> Sequence[Any]:
        """Return a new list containing all items from the iterable in random order."""
        return self._random.sample(population, len(population))


SGxRandom = Random()
