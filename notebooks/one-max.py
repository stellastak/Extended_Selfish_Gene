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

import sys
sys.path += ['../src']

from itertools import product
from math import inf
import numpy as np
import pandas as pd
from tqdm import tqdm

import sgx

results = pd.DataFrame(columns=['Allele', 'Size', 'Learning Rate', 'Generations'])

for problem_size in tqdm([10, 20], desc="PROBLEM SIZE", position=0, leave=None, ncols=0):
    fitness_function = sgx.fitness.FitnessFunction(lambda i: sum(i), best_fitness=problem_size, type_=sgx.fitness.Scalar)
    experiments = product(tqdm(np.linspace(1e-6, 0.2, 50), leave=False), range(20))
    for lr, _ in tqdm(list(experiments), position=1, leave=None, ncols=0):
        data = {'Allele': 'Categorical', 'Size': problem_size, 'Learning Rate': lr}
        genome = sgx.t.Genome([sgx.allele.Categorical([0, 1], learning_rate=lr) for _ in range(problem_size)])
        species = sgx.t.Species(genome=genome, fitness_function=fitness_function)
        archive = sgx.algorithms.sg(species, max_generation=5000, progress_bar=False)
        data['Generations'] = archive.items[0].generation
        results = results.append(data, ignore_index=True)

results.to_sql(name='base', con='sqlite:///one-max.sqlite3', if_exists='replace')

for problem_size in tqdm([10, 20], desc="PROBLEM SIZE", position=0, leave=None, ncols=0):
    fitness_function = sgx.fitness.FitnessFunction(lambda i: sum(i), best_fitness=problem_size, type_=sgx.fitness.Scalar)
    experiments = product(tqdm(np.linspace(1e-6, 0.2, 50), leave=False), range(20))
    for lr, _ in tqdm(list(experiments), position=1, leave=None, ncols=0):
        data = {'Allele': 'Sigmoid', 'Size': problem_size, 'Learning Rate': lr}
        genome = sgx.t.Genome([sgx.allele.Boolean(learning_rate=lr) for _ in range(problem_size)])
        species = sgx.t.Species(genome=genome, fitness_function=fitness_function)
        archive = sgx.algorithms.sg(species, max_generation=5000, progress_bar=False)
        data['Generations'] = archive.items[0].generation
        results = results.append(data, ignore_index=True)

results.to_sql(name='base', con='sqlite:///one-max.sqlite3', if_exists='append')
