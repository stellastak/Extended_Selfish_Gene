""""""""""""
Introduction
""""""""""""

What is SGX?
============

The Selfish Gene optimization algorithm (SG) is a population-less evolutionary algorithm
loosely inspired by the interpretation of the Darwinian theory given by the English
biologist Richard Dawkins and popularized as the Selfish Gene theory.
It enables a user to efficiently find the list parameters, either discrete symbols
or real numbers, that maximizes a given target function.

The original SG was an almost straightforward implementation of a though experiment,
only able to handle binary values; it was published in SAC98 as
`"The selfish gene algorithm: a new evolutionary optimization strategy" (F. Corno, M.S. Reorda, G. Squillero, 1998) <https://doi.org/10.1145/330560.330838>`_
and few month later, with some modifications, in ICEC98 as
`"A new evolutionary algorithm inspired by the selfish gene theory" (F. Corno, M.S. Reorda, G. Squillero, 1998) <https://ieeexplore.ieee.org/document/700092>`_.
The base algorithm was later discovered surprisingly similar to the Equilibrium Genetic Algorithm,
developed by Ari Juels, Shumeet Baluja, and Alistair Sinclair in 1993 and never published
-- see `"Lost gems of EC: the equilibrium genetic algorithm and the role of crossover" (Fernando G. Lobo, 2007) <https://doi.org/10.1145/1329465.1329468>`_.
Even more surprisingly, Georges Harik, Fernando Lobo, and David Golberg proposed a quite similar,
yet completely unrelated, algorithm in the very same ICEC98: `"The Compact Genetic Algorithm"
(G.R. Harik, F.G. Lobo, D.E. Goldberg, 1998) <https://ieeexplore.ieee.org/document/700083>`_.
Comprehensive background information on `"Estimation of Distribution Algorithms (EDAs) (Martin Pelikan, Mark W. Hauschild, Fernando G. Lobo, 2015) <https://link.springer.com/chapter/10.1007/978-3-662-43505-2_45>`_
can be found in an introduction by Lobo et al.

Since its appearance, the SG was demonstrated more robust than pure hill climbing,
reasonably efficient, and quite easy to implement. It was immediately exploited by practitioners
in many real-world applications, CAD problems; and by scholars for various test benches.
Moreover, the SG framework enabled the inclusions of tricks that made it effective in quite
a wider range of situations. The enhanced SG-Clans added to the basic SG a sort of recursive
evolution, inspired by the concept of allopatric speciation, to escape local optima.
Results were published in `"Optimizing deceptive functions with the SG-Clans algorithm" (F. Corno, M.S. Reorda, G. Squillero, 1999) <https://ieeexplore.ieee.org/document/785547>`_.
Non-binary encodings were eventually added in 2000s. Indeed, real-valued parameters was never included as
they never worked properly, although a draft paper titled "A population-less evolutionary algorithm
for real and integer optimization" mysteriously crawled its way up to semantic scholar.

Over the years, the algorithm was reimplemented by different researchers in different languages,
and a few brand new approaches derived from it (see Google Scholar's up-to-date references).
In 2016, a comprehensive review was published on IOPScience `"Selfish Gene Algorithm Vs Genetic Algorithm: A Review" (Ariff, Norharyati Md, Khalid, Noor Elaiza Abdul, Hashim, Rathiah, Noor, Noorhayati Mohamed, 2016) <https://iopscience.iop.org/article/10.1088/1757-899X/160/1/012098/pdf>`_.

Audience
========

The expected audience for SGX, a *'Quick n' Dirty'* numerical optimization,
includes computer scientists, engineers and practitioners.

* This evolutionary algorithm provides a *Sub-Optimal* result, which is **better than a "hill-climbing" algorithm**.
* It is a **real, industrial application** where fitness function is computationally intensive.
* **Real-time** application.
* SGX also provides an easy-to-use and **standard interface**.
* The code is **parallelizable**, which means that it can run in parallel multiple threads. There is no need to wait for everything to be completed. Some implementations might be Embarrassingly parallel (see `<https://en.wikipedia.org/wiki/Embarrassingly_parallel>`_).
* SGX is available as a `PyPi package <https://pypi.org/project/sgx/>`_ and it can be easily installed using `pip <https://en.wikipedia.org/wiki/Pip_%28package_manager%29>`_.
* The modular design allows scholars to extend SGX for custom application.