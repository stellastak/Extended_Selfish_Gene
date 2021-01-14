What is SGX?
============

The Selfish Gene optimization algorithm (SG) is a population-less evolutionary algorithm loosely inspired by the interpretation of the Darwinian theory given by the English biologist Richard Dawkins and popularized as the Selfish Gene theory. It enables a user to efficiently find the list parameters, either discrete symbols or real numbers, that maximizes a given target function.

The original SG was an almost straightforward implementation of a though experiment, only able to handle binary values; it was published in SAC98 as "The selfish gene algorithm: a new evolutionary optimization strategy" (DOI: 10.1145/330560.330838) and few month later, with some modifications, in ICEC98 as "A new evolutionary algorithm inspired by the selfish gene theory" (DOI: 10.1109/ICEC.1998.700092).

The base algorithm was later discovered surprisingly similar to the Equilibrium Genetic Algorithm, developed by Ari Juels, Shumeet Baluja, and Alistair Sinclair in 1993 and never published -- see "Lost gems of EC: the equilibrium genetic algorithm and the role of crossover" (DOI: 10.1145/1329465.1329468). Even more surprisingly, Georges Harik, Fernando Lobo, and David Golberg proposed a quite similar, yet completely unrelated, algorithm in the very same ICEC98: "The compact genetic algorithm" (DOI: 10.1109/ICEC.1998.700083). Comprehensive background information on estimation of distribution algorithms (EDAs) can be found in an introduction by Lobo et al. (DOI: 10.1007/978-3-662-43505-2_45).

Since its appearance, the SG was demonstrated more robust than pure hill climbing, reasonably efficient, and quite easy to implement. It was immediately exploited by practitioners in many real-world applications, CAD problems; and by scholars for various test benches. Moreover, the SG framework enabled the inclusions of tricks that made it effective in quite a wider range of situations. The enhanced SG-Clans added to the basic SG a sort of recursive evolution, inspired by the concept of allopatric speciation, to escape local optima. Results were published in "Optimizing deceptive functions with the SG-Clans algorithm" (DOI: 10.1109/CEC.1999.785547). Non-binary encodings were eventually added in 2000s. Indeed, real-valued parameters was never included as they never worked properly, although a draft paper titled "A population-less evolutionary algorithm for real and integer optimization" mysteriously crawled its way up to semantic scholar.

Over the years, the algorithm was reimplemented by different researchers in different languages, and a few brand new approaches derived from it (see Google Scholar's up-to-date references). In 2016, Norharyati Md Ariff, Noor Elaiza Abdul Khalid, Rathiah Hashim, and Noorhayati Mohamed Noor published a comprehensive review on IOPScience (DOI: 10.1088/1757-899X/160/1/012098).

Audience
========

The expected audience for SGX, a 'Quick n' Dirty' numerical optimization, includes computer scientists, engineers and practitioners.

* This evolutionary algorithm provides a Sub-Optimal result, which is better than a "hill-climbing" algorithm.
* It is a real, industrial application where fitness function is computationally intensive.
* Real-time application.
* SGX also provides an easy-to-use and standard interface.
* Parallelizable
* SGX is available as a `PyPi package <https://pypi.org/project/sgx/>`_ and it can be easily installed using `pip <https://en.wikipedia.org/wiki/Pip_%28package_manager%29>`_.
* The modular design allows scholars to extend SGX for custom application.