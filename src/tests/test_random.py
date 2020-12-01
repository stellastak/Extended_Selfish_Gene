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

import random
from sgx.utils.random import SGxRandom


def test_consistency():
    SGxRandom._random.seed(42)
    r0 = list()
    r1 = list()
    for _ in range(100):
        r0.append(SGxRandom.random())
        r1.append(random.random())
    assert r1 == r1

    SGxRandom._random.seed(42)
    r2 = [SGxRandom.random() for _ in range(100)]
    assert r0 == r2

    SGxRandom._random.seed(42)
    state = SGxRandom._random.getstate()
    r3 = [SGxRandom.random() for _ in range(100)]
    assert state != SGxRandom._random.getstate()
    SGxRandom._random.seed(42)
    assert state == SGxRandom._random.getstate()
    state_std = random.getstate()
    random.shuffle(r1)
    assert state_std != random.getstate()
    assert state == SGxRandom._random.getstate()
    r4 = [SGxRandom.random() for _ in range(100)]
    assert r3 == r4


def test_choice():
    for _ in range(1000):
        assert SGxRandom.choice([0, 1, 2, 3, 4], weights=[1, 0, 0, 0, 0]) == 0
        assert SGxRandom.choice([0, 1, 2, 3, 4], weights=[0, .25, .25, .25, .25]) != 0


def test_shuffled():
    assert list(range(1000)) == sorted(SGxRandom.shuffled(list(range(1000))))
