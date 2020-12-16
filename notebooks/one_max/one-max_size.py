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

results = pd.DataFrame(columns=['Allele', 'Size', 'Learning Rate', 'Generations', 'Fitness Calls'])
results1 = pd.DataFrame(columns=['Allele', 'Size', 'Learning Rate', 'Generations', 'Fitness Calls'])


for problem_size in tqdm([5,10,15,20], desc="PROBLEM SIZE", position=0, leave=None, ncols=0):
    fitness_function = sgx.fitness.FitnessFunction(lambda i: sum(i), best_fitness=problem_size, type_=sgx.fitness.Scalar)
    experiments = product(tqdm(np.linspace(0.1, 0.1, 1), leave=False), range(5))
    for lr, _ in tqdm(list(experiments), position=1, leave=None, ncols=0):
        data = {'Allele': 'Categorical', 'Size': problem_size, 'Learning Rate': lr , 'Generations' : None, 'Fitness Calls' : None}
        genome = sgx.t.Genome([sgx.allele.Categorical([0, 1], learning_rate=lr) for _ in range(problem_size)])
        species = sgx.t.Species(genome=genome, fitness_function=fitness_function)
        archive = sgx.algorithms.sg(species, max_generation=5000, progress_bar=False)
        data['Generations'] = archive.items[0].generation
        data['Fitness Calls'] = fitness_function.counter
        fitness_function.reset_counter()
        results = results.append(data, ignore_index=True)

    print(results)

for problem_size in tqdm([5,10,15,20], desc="PROBLEM SIZE", position=0, leave=None, ncols=0):
    fitness_function = sgx.fitness.FitnessFunction(lambda i: sum(i), best_fitness=problem_size, type_=sgx.fitness.Scalar)
    experiments = product(tqdm(np.linspace(0.1, 0.1, 1), leave=False), range(5))
    for lr, _ in tqdm(list(experiments), position=1, leave=None, ncols=0):
        data = {'Allele': 'Sigmoid', 'Size': problem_size, 'Learning Rate': lr , 'Generations' : None, 'Fitness Calls' : None}
        genome = sgx.t.Genome([sgx.allele.Categorical([0, 1], learning_rate=lr) for _ in range(problem_size)])
        species = sgx.t.Species(genome=genome, fitness_function=fitness_function)
        archive = sgx.algorithms.sg(species, max_generation=5000, progress_bar=False)
        data['Generations'] = archive.items[0].generation
        data['Fitness Calls'] = fitness_function.counter
        fitness_function.reset_counter()
        results = results.append(data, ignore_index=True)

    print(results)

sum_fitness = 0
sum_generations = 0
keys = results.keys()
index_of_last_row = results.size/len(keys)
for ind in results.index:
    if index_of_last_row-1 != ind:
        if results['Size'][ind] == results['Size'][ind+1]:
            sum_fitness += results['Fitness Calls'][ind]
            sum_generations += results['Generations'][ind]
        else:
            if results['Allele'][ind]=='Categorical':
                data = {'Allele': 'Categorical', 'Size': results['Size'][ind], 'Learning Rate': results['Learning Rate'][ind],
                        'Generations': None, 'Fitness Calls': None}
            elif results['Allele'][ind]=='Sigmoid':
                data = {'Allele': 'Sigmoid', 'Size': results['Size'][ind], 'Learning Rate': results['Learning Rate'][ind],
                        'Generations': None, 'Fitness Calls': None}
            sum_fitness += results['Fitness Calls'][ind]
            sum_generations += results['Generations'][ind]
            data['Generations'] = int(sum_generations)
            data['Fitness Calls'] = int(sum_fitness)
            results1 = results1.append(data, ignore_index=True)
            sum_fitness = 0
            sum_generations = 0
    else:
        if results['Allele'][ind] == 'Categorical':
            data = {'Allele': 'Categorical', 'Size': results['Size'][ind],
                    'Learning Rate': results['Learning Rate'][ind],
                    'Generations': None, 'Fitness Calls': None}
        elif results['Allele'][ind] == 'Sigmoid':
            data = {'Allele': 'Sigmoid', 'Size': results['Size'][ind], 'Learning Rate': results['Learning Rate'][ind],
                    'Generations': None, 'Fitness Calls': None}
        sum_fitness = +results['Fitness Calls'][ind]
        sum_generations += results['Generations'][ind]
        data['Generations'] = int(sum_generations)
        data['Fitness Calls'] = int(sum_fitness)
        results1 = results1.append(data, ignore_index=True)
        sum_fitness = 0
        sum_generations = 0
print(results1)

results1.to_sql(name='base', con='sqlite:///one-max_size.sqlite3', if_exists='replace')