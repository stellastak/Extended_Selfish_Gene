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

from typing import Sequence, Any, Type
from math import isclose

from ..utils import logging
from numbers import Number
from .base import Fitness


class Scalar(Fitness, float):
    """A single numeric value -- Larger is better."""
    pass


class Integer(Fitness, int):
    """A single numeric value -- Larger is better."""
    pass


class Approximate(Fitness, float):
    """A single, floating-point value with approximate equality -- Larger is better."""

    def __init__(self, argument, rel_tol: float = 1e-09, abs_tol: float = 0):
        """See the documentation of math.isclose() and PEP485."""
        super(Approximate, self).__init__()
        self._rel_tol = rel_tol
        self._abs_tol = abs_tol

    def decorate(self) -> str:
        """Represent the individual fitness value with a nice string."""
        return str(float(self)) + '≈'

    def is_distinguishable(self, other: 'Fitness') -> bool:
        """Check whether some differences from the other Fitness may be perceived."""
        self.check_comparable(other)
        return not isclose(float(self), float(other), rel_tol=self._rel_tol, abs_tol=self._abs_tol)

    def is_fitter(self, other: 'Fitness') -> bool:
        """Check whether fitter than the other."""
        self.check_comparable(other)
        return self != other and float(self) > float(other)

    def check_comparable(self, other: 'Approximate'):
        """Checks if the fitness is able to be compared."""
        super().check_comparable(other)
        assert self._abs_tol == other._abs_tol, f"Can't is_fitter Fitness Floats with different absolute tolerance ({float(self)}±{self._abs_tol} vs. {float(other)}±{other._abs_tol})"
        assert self._rel_tol == other._rel_tol, f"Can't is_fitter Fitness Floats with different relative tolerance ({float(self)}±{self._rel_tol}r vs. {float(other)}±{other._rel_tol}r)"


# VECTORS


class Vector(Fitness):
    """A generic vector of Fitness values.

    fitness_type is the subtype, **kwargs are passed to fitness init

    Examples:
        f1 = sgx.fitness.Vector([23, 10], fitness_type=Approximate, abs_tol=.1)
        f2 = sgx.fitness.Vector([23, 10], fitness_type=Approximate, abs_tol=.001)

        f1 > sgx.fitness.Vector([23, 9.99], fitness_type=Approximate, abs_tol=.1) is False
        f2 > sgx.fitness.Vector([23, 9.99], fitness_type=Approximate, abs_tol=.001) is True

    """

    def __init__(self, value: Sequence, fitness_type: Type[Fitness] = Scalar, **kwargs):
        self._values = tuple(fitness_type(e, **kwargs) for e in value)
        self.run_paranoia_checks()

    def is_distinguishable(self, other: 'Vector') -> bool:
        """Check whether some differences from the other Fitness may be perceived."""
        self.check_comparable(other)
        return any(e1 != e2 for e1, e2 in zip(self._values, other._values))

    def is_fitter(self, other: 'Fitness') -> bool:
        """Check whether fitter than the other."""
        self.check_comparable(other)
        return Vector.compare_vectors(self._values, other._values) > 0

    @staticmethod
    def compare_vectors(v1: Sequence[Fitness], v2: Sequence[Fitness]) -> int:
        """Compare Fitness values in v1 and v2.

        Args:
            v1: The first fitness vector.
            v2: The second fitness vector.

        Returns:
             -1 if v1 < v2; +1 if v1 > v2; 0 if v1 == v2
        """
        for e1, e2 in zip(v1, v2):
            if e1 > e2:
                return 1
            elif e2 > e1:
                return -1
        return 0

    def decorate(self) -> str:
        """Represent the individual fitness value with a nice string."""
        return ', '.join(e.decorate() for e in self._values)

    def check_comparable(self, other: 'Vector'):
        """Checks if the fitness is able to be compared."""
        super().check_comparable(other)
        assert len(self._values) == len(
            other._values), f"Can't is_fitter Fitness Vectors of different size ({self} vs. {other})"

    def __iter__(self):
        return iter(self._values)

    def __hash__(self):
        return hash(self._values)
