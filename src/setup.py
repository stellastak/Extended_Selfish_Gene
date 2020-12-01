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

import setuptools
from sgx import __name__, __version__

with open('pypi-description.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

OPTIONAL = ['coloredlogs', 'matplotlib', 'psutil']
with open('requirements.txt', 'r', encoding='utf-8') as fh:
    requirements = [r for r in fh.readlines() if not any(o in r for o in OPTIONAL)]

setuptools.setup(
    name=__name__,
    version=__version__,
    author="Giovanni Squillero",
    author_email="squillero@polito.it",
    license="Apache-2.0",
    description="A population-less EA loosely inspired by a cool interpretation of the Darwinian theory",
    long_description=long_description,
    #long_description_content_type="text/x-rst",
    long_description_content_type='text/markdown',
    url="https://github.com/squillero/sgx",
    project_urls={
        'Bug Tracker': "https://github.com/squillero/sgx/issues",
        #'Documentation': "https://microgp4.readthedocs.io/en/pre-alpha/",
        'Source Code': "https://github.com/squillero/sgx",
    },
    keywords="optimization evolutionary-algorithm computational-intelligence",
    packages=setuptools.find_packages(),
    package_dir={'': '.'},
    package_data={'': ['requirements.txt', 'pypi-description.md']},
    data_files=[('.', ['requirements.txt', 'pypi-description.md'])],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Mathematics",
        "License :: OSI Approved :: Apache Software License"
    ],
    install_requires=requirements,
)
