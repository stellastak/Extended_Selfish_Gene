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

import warnings

from ..utils import logging
from ..base import Pedantic, Paranoid


class Fitness(Pedantic, Paranoid):
    """Fitness of a phenotype, handle multiple formats (eg. scalar, tuple).

    The class also redefines the relational operator in order to handle different types of optimization
    (eg. maximization, minimization) and to provide limited support to more complex scenarios (eg. multi-objective optimization)

    Equalities ('==' and '!=') are based on `is_distinguishable`.

    Single angular-bracket operators ('>', '<', '>=', and '<=') are based on `is_fitter` and may be randomized
    (the result may not be reproducible).

    Double angular-bracket operators ('>>' and '<<') are based on `is_dominant` and the result is stable. By default
    `is_dominant` is defined as `is_fitter`.

    When subclassing, one should only redefine `is_fitter`, and optionally `is_distinguishable` and `is_dominant`;
    `is_dominant` must be changed if `is_fitter` is randomized (the result is uncertain).

    Additional sanity checks should be added to `check_comparable`. Subclasses may redefine the `decorate` method to
    change the values appearance.
    """

    def is_distinguishable(self, other: 'Fitness') -> bool:
        """Check whether some differences from the other Fitness may be perceived."""
        self.check_comparable(other)
        return super().__ne__(other)

    def is_fitter(self, other: 'Fitness') -> bool:
        """Check whether fitter than the other (result may be accidental)."""
        self.check_comparable(other)
        return super().__gt__(other)

    def is_dominant(self, other: 'Fitness') -> bool:
        """Check whether dominates the other (result is certain)."""
        self.check_comparable(other)
        return self.is_fitter(other)

    def decorate(self) -> str:
        """Represent the individual fitness value with a nice string."""
        return f"{super().__str__()}"

    # FINAL/WARNINGS

    def __eq__(self, other: 'Fitness') -> bool:
        return not self.is_distinguishable(other)

    def __ne__(self, other: 'Fitness') -> bool:
        return self.is_distinguishable(other)

    def __gt__(self, other: 'Fitness') -> bool:
        return self.is_fitter(other)

    def __lt__(self, other: 'Fitness') -> bool:
        return other.is_fitter(self)

    def __ge__(self, other: 'Fitness') -> bool:
        return not self.__lt__(other)

    def __le__(self, other: 'Fitness') -> bool:
        return not self.__gt__(other)

    def __rshift__(self, other: 'Fitness') -> bool:
        return self.is_dominant(other)

    def __lshift__(self, other: 'Fitness') -> bool:
        return other.is_dominant(self)

    def __str__(self):
        # Double parentheses: ⸨ ⸩  (U+2E28, U+2E29)
        # White parentheses: ⦅ ⦆  (U+2985, U+2986)
        # Fullwidth white parentheses:｟ ｠ (U+FF5F, U+FF60)
        return f"⸨{self.decorate()}⸩"

    def __hash__(self) -> int:
        return super().__hash__()

    def check_comparable(self, other: 'Fitness'):
        assert isinstance(other, Fitness), f"Can't is_fitter a Fitness against a different type ({type(other)})"
        assert other.run_paranoia_checks()
        assert self.__class__ == other.__class__, f"Can't is_fitter Fitness values of different types ({type(self)} vs. {type(other)})"

    def run_paranoia_checks(self) -> bool:
        return super().run_paranoia_checks()

    def is_valid(self, fitness: 'Fitness') -> bool:
        try:
            self.check_comparable(fitness)
        except AssertionError:
            return False
        return True


def reversed(fitness_class: 'Fitness') -> 'Fitness':
    """Reverse fitness class turning a maximization problem into a minimization one."""
    assert isinstance(
        fitness_class,
        type), f"Only <class 'sgx.t.Fitness'> can be reversed. Found an object of type {type(fitness_class)}."
    assert issubclass(fitness_class, Fitness), f"Only <class 'sgx.t.Fitness'> can be reversed. Found {fitness_class}."

    class r(fitness_class):

        def __gt__(self, other: 'Fitness') -> bool:
            return fitness_class(other) > fitness_class(self)

        def __rshift__(self, other: 'Fitness') -> bool:
            return fitness_class(other) >> fitness_class(self)

    return r
