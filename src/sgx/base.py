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

__all__ = ['Genome', 'Genotype', 'Pedantic', 'Paranoid']

from typing import Any, Sequence, Tuple, Hashable, Callable
from abc import ABC, abstractmethod

from .allele import base


class Paranoid():
    """Abstract class: Paranoid classes do implement `run_paranoia_checks()`."""

    def run_paranoia_checks(self) -> bool:
        """Check the internal consistency of a "paranoid" object.

        The function should be overridden by the sub-classes to implement the
        required, specific checks. It always returns `True`, but throws an
        exception whenever an inconsistency is detected.

        **Notez bien**: Sanity checks may be computationally intensive,
        paranoia checks are not supposed to be used in production environments
        (i.e., when `-O` is used for compiling). Their typical usage is:
        `assert foo.run_paranoia_checks()`

        Returns:
            True (always)

        Raise:
            AssertionError if some internal data structure is incoherent
        """
        return True


class Pedantic(ABC):
    """Abstract class: Pedantic classes do implement `is_valid()`."""

    @abstractmethod
    def is_valid(self, obj: Any) -> bool:
        """Check an object against a specification.

        The function may be used to check a value against a parameter definition, a node against a section definition).

        Returns:
            True if the object is valid, False otherwise
        """
        raise NotImplementedError("Abstract method not implemented")


class Genotype(tuple, Paranoid):
    """A tuple containing the organism’s actual genes (their values)."""

    def __init__(self, *args):
        super().__init__()
        assert self.run_paranoia_checks()

    def squeeze(self):
        return str.join('', [str(_) for _ in tuple(self)])

    def __str__(self):
        return f"[{str.join(', ', [repr(_) for _ in tuple(self)])}]"

    def __repr__(self):
        return object.__repr__(self)

    def run_paranoia_checks(self) -> bool:
        return super().run_paranoia_checks()


class Genome(list, Pedantic, Paranoid):
    """A tuple of Alleles, each one specifying a set of alternative genes."""

    def __init__(self, *args):
        super().__init__(*args)
        assert self.run_paranoia_checks()
        self._is_squeezable = all(a.is_squeezable for a in list(self))

    def __repr__(self):
        return object.__repr__(self)

    @property
    def is_squeezable(self):
        return self._is_squeezable

    def run_paranoia_checks(self) -> bool:
        for i, a in enumerate(self):
            assert isinstance(a, base.Allele), f"Locus[{i}] is not <class 'sgx.allele.Allele'> > but {type(a)}"
        return super().run_paranoia_checks()

    def is_valid(self, genotype: Genotype) -> bool:
        if any(not a.is_valid(g) for a, g in zip(list(self), genotype)):
            return False
        return super().is_valid(genotype)

    def format_genotype(self, genotype: Genotype) -> str:
        if self._is_squeezable:
            return genotype.squeeze()
        else:
            return str(genotype)
