""""""
Allele
""""""

.. toctree::
   :caption: Allele
   :maxdepth: 4

An allele can be one of the following types:

- a :mod:`sgx.allele.boolean` which is either "1" or "0".
- a :mod:`sgx.allele.categorical` (for example "R", "G", "B")

Base Allele class
=================

:mod:`sgx.allele.base`

.. automodule:: sgx.allele.base
   :members:

Boolean Allele class
====================

:mod:`sgx.allele.boolean`

.. automodule:: sgx.allele.boolean
   :members:

Categorical Allele class
========================

:mod:`sgx.allele.categorical`

.. automodule:: sgx.allele.categorical
   :members:

--------------------------------

"""""""
Fitness
"""""""

.. toctree::
   :caption: Fitness
   :maxdepth: 4


Base fitness class
==================

:mod:`sgx.fitness.base`

.. automodule:: sgx.fitness.base
   :members:

Fitness Function class
======================

:mod:`sgx.fitness.function`

.. automodule:: sgx.fitness.function
   :members:

---------------------------

Multi-Objective class
=====================

:mod:`sgx.fitness.multi_objective`

.. automodule:: sgx.fitness.multi_objective
   :members:

----------------------------

Simple class
============

:mod:`sgx.fitness.simple`

.. automodule:: sgx.fitness.simple
   :members:

----------------------------

"""""
Utils
"""""

.. toctree::
   :caption: Utils
   :maxdepth: 4

CPU_time
========

:mod:`sgx.utils.cpu_time`

.. automodule:: sgx.utils.cpu_time
   :members:

Jupyter Support
===============

:mod:`sgx.utils.jupyter_support`

.. automodule:: sgx.utils.jupyter_support
   :members:

Logging
=======

:mod:`sgx.utils.logging`

.. automodule:: sgx.utils.logging
   :members:

Random class
============

:mod:`sgx.utils.random`

.. automodule:: sgx.utils.random
   :members:


Archive class
=============

:mod:`sgx.archive`

.. automodule:: sgx.archive
   :imported-members:
   :members:
   :undoc-members:
   :show-inheritance:

Base class
==========

:mod:`sgx.base`

.. automodule:: sgx.base
   :members:

Species class
=============

:mod:`sgx.species`

.. automodule:: sgx.species
   :members:

------------------------

""""""""""""""""""""""""
Modular Design Rationale
""""""""""""""""""""""""

**Object-oriented programming (OOP)** is based on the concept of "objects", which can contain data and code:
data in the form of field, and code, in the form of procedures (often known as methods).
A feature of objects is that an object's own procedures can access and often modify the data fields of itself.
In OOP, computer programs are designed by making them out of objects that interact with one another.

Python language is a multi-paradigm and supports object-oriented programming to a greater degree, typically
in combination with imperative, procedural programming.

+---------------------------------------------------------------------+
|                     Extended Selfish Gene Optimizer                 |
+==================================+==================================+
|            Genotype              |            Fitness               |
+----------------------------------+-----------------+----------------+
|             Genome               |Single-Objective | Multi-Objective|
+----------------------------------+-----------------+----------------+
|             Allele               |   -Int          |     -Char      |
+---------------+------------------+   -Float        |     -Float     |
|    Boolean    |   Categorical    |   -Double       |      etc.      |
+-------+-------+-----+-----+------+                 |                |
|  -0   |  -1   |  -R |  -G |  -B  |                 |                |
+-------+-------+-----+-----+------+-----------------+----------------+