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

from typing import Optional, Sequence, Hashable, Union, Dict, Tuple
from math import isclose

from ..utils import logging
from ..utils.random import SGxRandom

from .base import Allele


class Categorical(Allele):
    DEFAULT_LEARNING_RATE = .001

    def __init__(self,
                 alternatives: Sequence[Hashable],
                 weights: Optional[Union[Sequence[float], dict]] = None,
                 learning_rate: Optional[float] = None):
        if learning_rate is None:
            learning_rate = Categorical.DEFAULT_LEARNING_RATE
        assert 0 < learning_rate < 1, f"Learning rate must be ]0, 1[: {learning_rate}"
        alternatives = list(alternatives)
        assert len(alternatives) == len(set(alternatives)), f"Alternatives must be uniques: {alternatives}"
        if weights is None:
            weights = [1 / len(alternatives) for a in alternatives]
        elif isinstance(weights, dict):
            assert all(
                k in alternatives
                for k in weights), f"All keys in weight must be valid alternatives: {weights.keys()} vs. {alternatives}"
            weights = [weights[a] if a in weights else None for a in alternatives]
        if len(weights) < len(alternatives):
            weights += [None] * (len(alternatives) - len(weights))
        assert len(alternatives) == len(
            weights
        ), f"Number of alternatives and number of weights must be identical: {len(alternatives)} vs. {len(weights)}"
        assert all(
            0 <= w <= 1 for w in [w for w in weights if w is not None]), f"Each weights must be in [0, 1]: {weights}"
        assert sum(w for w in weights if w is not None) <= 1, f"Partial weights sum must be less 1 ({weights})"
        if None in weights:
            missing = (1 - sum(w for w in weights if w is not None)) / weights.count(None)
            weights = [w if w is not None else missing for w in weights]
        assert isclose(sum(weights), 1), f"Weights sum must be 1: sum({weights}) = {sum(weights)}"
        self._alternatives = tuple(alternatives)
        self._weights = list(weights)
        self._learning_rate = learning_rate

    def sample(self, sample_type: Optional[str] = Allele.DEFAULT_SAMPLE_TYPE) -> Hashable:
        """Sample.

        Args:
            sample_type: The type of sample (sample (default), uniform, mode).
        """
        if sample_type == Allele.SAMPLE_TYPE__SAMPLE:
            return SGxRandom.choice(self._alternatives, weights=self._weights)
        elif sample_type == Allele.SAMPLE_TYPE__UNIFORM:
            return SGxRandom.choice(self._alternatives, weights=None)
        elif sample_type == Allele.SAMPLE_TYPE__MODE:
            return self._alternatives[self._weights.index(max(self._weights))]
        else:
            assert sample_type in Allele.VALID_SAMPLE_TYPES, f"Unknown sample type: {sample_type!r} vs. {Allele.VALID_SAMPLE_TYPES}"

    def update(self, winner: Hashable, loser: Hashable) -> None:
        """Updates the winner and the loser Genotype, so as to modify the new Learning Rate.

        Args:
            winner: The genotype of the better solution.
            loser: The genotype of the worse solution.
        """
        assert self.is_valid(winner), f"The winner must be a valid alternative: {winner!r} vs. {self._alternatives}"
        assert self.is_valid(loser), f"The loser must be a valid alternative: {loser!r} vs. {self._alternatives}"
        wi = self._alternatives.index(winner)
        li = self._alternatives.index(loser)
        update = self._learning_rate
        update = min(update, 1 - self._weights[wi])
        update = min(update, self._weights[li])
        self._weights[wi] += update
        self._weights[li] -= update
        assert self.run_paranoia_checks()

    @property
    def possible_values(self) -> Optional[Tuple[str]]:
        """Possible values of the allele. None if not reasonably applicable (eg. a float)"""
        return self._alternatives

    def describe(self) -> str:
        """Pretty describes the current categorical allele."""
        return '｜'.join(f'{a!r}/{w:.2}' for a, w in zip(self._alternatives, self._weights))

    def is_valid(self, value: Hashable) -> bool:
        """Checks if the allele is categorical."""
        return value in self._alternatives

    def run_paranoia_checks(self) -> bool:
        """Returns True, if all tests are passed."""
        assert len(self._alternatives) == len(set(
            self._alternatives)), f"Alternatives must be uniques: {self._alternatives}"
        assert len(self._alternatives) == len(
            self._weights
        ), f"Number of alternatives and number of weights must be identical: {len(self._alternatives)} vs. {len(self._weights)}"
        assert all(0 <= w <= 1 for w in self._weights), f"Each weights must be in [0, 1]: {self._weights}"
        assert isclose(sum(self._weights), 1), f"Weights sum must be 1: sum({self._weights}) = {sum(self._weights)}"
        return super().run_paranoia_checks()
